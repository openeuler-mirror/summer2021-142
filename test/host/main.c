#include <stdio.h>
#include <unistd.h>
#include <linux/limits.h>
#include "enclave.h"
#include "helloworld_u.h"
#include "string.h"

#define BUF_LEN 32


int printout(char* buf)
{
    printf("%s", buf);
    return 0;
}

int main()
{
    int  retval = 0;
    char* path = PATH;
    char buf[BUF_LEN];
    cc_enclave_t* context = NULL;
    context = (cc_enclave_t*)malloc(sizeof(cc_enclave_t));
    if (!context) {
        return CC_ERROR_OUT_OF_MEMORY;
    }
    cc_enclave_result_t res = CC_FAIL;

    printf("Create secgear enclave\n");

    char real_p[PATH_MAX];
    /* check file exists, if not exist then use absolute path */
    if (realpath(path, real_p) == NULL) {
        if (getcwd(real_p, sizeof(real_p)) == NULL) {
            printf("Cannot find enclave.sign.so");
            goto end;
        }
        if (PATH_MAX - strlen(real_p) <= strlen("/enclave.signed.so")) {
            printf("Failed to strcat enclave.sign.so path");
            goto end;
        }
        (void)strcat(real_p, "/enclave.signed.so");
    }
    //创建enclave
    res = cc_enclave_create(real_p, AUTO_ENCLAVE_TYPE, 0, SECGEAR_DEBUG_FLAG, NULL, 0, context);
    if (res != CC_SUCCESS) {
        printf("Create enclave error\n");
        goto end;
    }
    //调用getstring，非安全侧输出
    res = get_string(context, &retval, buf);
    if (res != CC_SUCCESS || retval != (int)CC_SUCCESS) {
        printf("Ecall enclave error\n");
    }
    else {
        printf("print: %s\n", buf);
    }
    //销毁enclave
    res = cc_enclave_destroy(context);
    if (res != CC_SUCCESS) {
        printf("Destroy enclave error\n");
    }
    //free缓存
end:
    free(context);
    return res;
}
