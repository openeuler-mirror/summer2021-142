#include <stdio.h>
#include <string.h>
#include "helloworld_t.h"

#define TA_HELLO_WORLD        "secgear hello world!"
#define BUF_MAX 32
int get_string(char* buf)
{
    strncpy(buf, TA_HELLO_WORLD, strlen(TA_HELLO_WORLD) + 1);
    PrintInfo(buf);
    cc_enclave_result_t res = CC_FAIL;
    res = printout(&retval, buf)
    if (res != CC_SUCCESS || retval != (int)CC_SUCCESS) {
        printf("Ocall error\n");
    }
    return 0;
}
