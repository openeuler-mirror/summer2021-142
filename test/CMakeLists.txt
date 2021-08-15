project(learning  C)

set(CMAKE_C_STANDARD 99)

set(CURRENT_ROOT_PATH ${CMAKE_CURRENT_SOURCE_DIR})

#set edl name
set(EDL_FILE learning.edl)
set(CODEGEN codegen)

if(CC_GP)
    set(CODETYPE trustzone)
    set(UUID f68fd704-6eb1-4d14-b218-722850eb3ef0)
    add_definitions(-DPATH="/data/${UUID}.sec")
endif()

if(CC_SGX)
    set(CODETYPE sgx)
    add_definitions(-DPATH="${CMAKE_CURRENT_BINARY_DIR}/enclave/enclave.signed.so")
endif()

add_subdirectory(${CURRENT_ROOT_PATH}/enclave)
add_subdirectory(${CURRENT_ROOT_PATH}/host)
