Name:     graphene
Version:  1.2_rc1
Release:  1%{?dist}
Summary:  The "graphene" program
License:  GPLv3+
URL:      https://github.com/gramineproject/graphene
Source0:  https://github.com/gramineproject/graphene/archive/refs/tags/v1.2-rc1.tar.gz


%description
The "graphene" program, done with all bells and whistles of a proper FOSS 
project, including configuration, build, internationalization, help files, etc.


%prep
%setup -n graphene-1.2-rc1

%build  
make
meson setup build/ --buildtype=release -Ddirect=enabled -Dsgx=disabled
ninja -C build/

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/
mkdir -p %{buildroot}/usr/local/bin/
mkdir -p %{buildroot}/usr/local/lib64/graphene/runtime/glibc/
mkdir -p %{buildroot}/usr/local/lib64/python3.8/site-packages/graphenelibos/
mkdir -p %{buildroot}/usr/local/lib64/graphene/direct/gdb_integration/common/
cp -p %_builddir/graphene-1.2-rc1/Pal/src/host/Linux/gdb_integration/graphene_linux_gdb.py %{buildroot}/usr/local/lib64/graphene/direct/gdb_integration
cp -p %_builddir/graphene-1.2-rc1/Pal/src/host/Linux/../../../gdb_integration/graphene.gdb %{buildroot}/usr/local/lib64/graphene/direct/gdb_integration/common
cp -p %_builddir/graphene-1.2-rc1/Pal/src/host/Linux/../../../gdb_integration/pagination_gdb.py %{buildroot}/usr/local/lib64/graphene/direct/gdb_integration/common
cp -p %_builddir/graphene-1.2-rc1/Pal/src/host/Linux/../../../gdb_integration/debug_map_gdb.py %{buildroot}/usr/local/lib64/graphene/direct/gdb_integration/common
cp -p %_builddir/graphene-1.2-rc1/build/Pal/src/host/Linux/libpal.so %{buildroot}/usr/local/lib64/graphene/direct
cp -p %_builddir/graphene-1.2-rc1/build/Pal/src/host/Linux/libpal.a %{buildroot}/usr/local/lib64/graphene/direct
cp -p %_builddir/graphene-1.2-rc1/build/LibOS/shim/src/libsysdb.so %{buildroot}/usr/local/lib64/graphene
cp -p %_builddir/graphene-1.2-rc1/LibOS/glibc-build/csu/crt1.o %{buildroot}/usr/local/lib64/graphene/runtime/glibc
cp -p %_builddir/graphene-1.2-rc1/LibOS/glibc-build/csu/crti.o %{buildroot}/usr/local/lib64/graphene/runtime/glibc
cp -p %_builddir/graphene-1.2-rc1/LibOS/glibc-build/csu/crtn.o %{buildroot}/usr/local/lib64/graphene/runtime/glibc
cp -p %_builddir/graphene-1.2-rc1/LibOS/glibc-build/dlfcn/libdl.so.2 %{buildroot}/usr/local/lib64/graphene/runtime/glibc
cp -p %_builddir/graphene-1.2-rc1/LibOS/glibc-build/libc.so %{buildroot}/usr/local/lib64/graphene/runtime/glibc
cp -p %_builddir/graphene-1.2-rc1/LibOS/glibc-build/libc.so.6 %{buildroot}/usr/local/lib64/graphene/runtime/glibc
cp -p %_builddir/graphene-1.2-rc1/LibOS/glibc-build/login/libutil.so.1 %{buildroot}/usr/local/lib64/graphene/runtime/glibc
cp -p %_builddir/graphene-1.2-rc1/LibOS/glibc-build/math/libm.so.6 %{buildroot}/usr/local/lib64/graphene/runtime/glibc
cp -p %_builddir/graphene-1.2-rc1/LibOS/glibc-build/mathvec/libmvec.so.1 %{buildroot}/usr/local/lib64/graphene/runtime/glibc
cp -p %_builddir/graphene-1.2-rc1/LibOS/glibc-build/nis/libnsl.so.1 %{buildroot}/usr/local/lib64/graphene/runtime/glibc
cp -p %_builddir/graphene-1.2-rc1/LibOS/glibc-build/nptl/libpthread.so.0 %{buildroot}/usr/local/lib64/graphene/runtime/glibc
cp -p %_builddir/graphene-1.2-rc1/LibOS/glibc-build/nptl_db/libthread_db.so.1 %{buildroot}/usr/local/lib64/graphene/runtime/glibc
cp -p %_builddir/graphene-1.2-rc1/LibOS/glibc-build/nss/libnss_compat.so.2 %{buildroot}/usr/local/lib64/graphene/runtime/glibc
cp -p %_builddir/graphene-1.2-rc1/LibOS/glibc-build/nss/libnss_db.so.2 %{buildroot}/usr/local/lib64/graphene/runtime/glibc
cp -p %_builddir/graphene-1.2-rc1/LibOS/glibc-build/nss/libnss_files.so.2 %{buildroot}/usr/local/lib64/graphene/runtime/glibc
cp -p %_builddir/graphene-1.2-rc1/LibOS/glibc-build/resolv/libanl.so.1 %{buildroot}/usr/local/lib64/graphene/runtime/glibc
cp -p %_builddir/graphene-1.2-rc1/LibOS/glibc-build/resolv/libnss_dns.so.2 %{buildroot}/usr/local/lib64/graphene/runtime/glibc
cp -p %_builddir/graphene-1.2-rc1/LibOS/glibc-build/resolv/libresolv.so.2 %{buildroot}/usr/local/lib64/graphene/runtime/glibc
cp -p %_builddir/graphene-1.2-rc1/LibOS/glibc-build/rt/librt.so.1 %{buildroot}/usr/local/lib64/graphene/runtime/glibc
cp -p %_builddir/graphene-1.2-rc1/LibOS/glibc-build/elf/ld-linux-x86-64.so.2 %{buildroot}/usr/local/lib64/graphene/runtime/glibc
cp -p %_builddir/graphene-1.2-rc1/build/Runtime/graphene-direct %{buildroot}/usr/local/bin
cp -p %_builddir/graphene-1.2-rc1/build/python/graphenelibos/__init__.py %{buildroot}/usr/local/lib64/python3.8/site-packages/graphenelibos
cp -p %_builddir/graphene-1.2-rc1/python/graphenelibos/manifest.py %{buildroot}/usr/local/lib64/python3.8/site-packages/graphenelibos
cp -p %_builddir/graphene-1.2-rc1/python/graphene-manifest %{buildroot}/usr/local/bin
cp -r %_builddir/graphene-1.2-rc1/* %{buildroot}

%files
/build/*                  
/debugsources.list     
/Makefile           
/Scripts/*
/common/*                 
/Documentation/*         
/meson.build        
/tests/*
/CONTRIBUTING.rst       
/elfbins.list          
/meson_options.txt  
/Tools/*
/DCO                    
/Examples/*              
/Pal/*                
/usr/*
/debugfiles.list        
/LibOS/*               
/python/*
/debuglinks.list        
/LICENSE.addendum.txt  
/README.rst
/debugsourcefiles.list  
/LICENSE.txt           
/Runtime/*
/Documentation/.gitignore
/Examples/.gitignore
/LibOS/.gitignore
/Runtime/.gitignore
/Tools/.gitignore
/build/.ninja_deps
/build/.ninja_log
/tests/.gitignore



%changelog
* Fri Jul 9 2021 - 1.2-rc1
- Update to 1.1
