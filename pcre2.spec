#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x9766E084FB0F43D8 (ph10@cam.ac.uk)
#
Name     : pcre2
Version  : 10.37
Release  : 47
URL      : https://sourceforge.net/projects/pcre/files/pcre2/10.37/pcre2-10.37.tar.gz
Source0  : https://sourceforge.net/projects/pcre/files/pcre2/10.37/pcre2-10.37.tar.gz
Source1  : https://sourceforge.net/projects/pcre/files/pcre2/10.37/pcre2-10.37.tar.gz.sig
Summary  : PCRE2 - Perl compatible regular expressions C library (2nd API) with 32 bit character support
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pcre2-bin = %{version}-%{release}
Requires: pcre2-filemap = %{version}-%{release}
Requires: pcre2-lib = %{version}-%{release}
Requires: pcre2-license = %{version}-%{release}
Requires: pcre2-man = %{version}-%{release}
BuildRequires : bzip2-dev
BuildRequires : pkgconfig(valgrind)
BuildRequires : zlib-dev

%description
------------------------------------------------------------------
PCRE2 is a re-working of the original PCRE1 library to provide an entirely new
API. Since its initial release in 2015, there has been further development of
the code and it now differs from PCRE1 in more than just the API. There are new
features, and the internals have been improved. The original PCRE1 library is
now obsolete and should not be used in new projects. The latest release of
PCRE2 is available in three alternative formats from:

%package bin
Summary: bin components for the pcre2 package.
Group: Binaries
Requires: pcre2-license = %{version}-%{release}
Requires: pcre2-filemap = %{version}-%{release}

%description bin
bin components for the pcre2 package.


%package dev
Summary: dev components for the pcre2 package.
Group: Development
Requires: pcre2-lib = %{version}-%{release}
Requires: pcre2-bin = %{version}-%{release}
Provides: pcre2-devel = %{version}-%{release}
Requires: pcre2 = %{version}-%{release}

%description dev
dev components for the pcre2 package.


%package doc
Summary: doc components for the pcre2 package.
Group: Documentation
Requires: pcre2-man = %{version}-%{release}

%description doc
doc components for the pcre2 package.


%package filemap
Summary: filemap components for the pcre2 package.
Group: Default

%description filemap
filemap components for the pcre2 package.


%package lib
Summary: lib components for the pcre2 package.
Group: Libraries
Requires: pcre2-license = %{version}-%{release}
Requires: pcre2-filemap = %{version}-%{release}

%description lib
lib components for the pcre2 package.


%package license
Summary: license components for the pcre2 package.
Group: Default

%description license
license components for the pcre2 package.


%package man
Summary: man components for the pcre2 package.
Group: Default

%description man
man components for the pcre2 package.


%prep
%setup -q -n pcre2-10.37
cd %{_builddir}/pcre2-10.37
pushd ..
cp -a pcre2-10.37 buildavx2
popd

%build
## build_prepend content
export CFLAGS="$CFLAGS -mshstk"
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656310256
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
export FCFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
export FFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
export CFLAGS_GENERATE="$CFLAGS -fprofile-generate -fprofile-dir=/var/tmp/pgo -fprofile-update=atomic "
export FCFLAGS_GENERATE="$FCFLAGS -fprofile-generate -fprofile-dir=/var/tmp/pgo -fprofile-update=atomic "
export FFLAGS_GENERATE="$FFLAGS -fprofile-generate -fprofile-dir=/var/tmp/pgo -fprofile-update=atomic "
export CXXFLAGS_GENERATE="$CXXFLAGS -fprofile-generate -fprofile-dir=/var/tmp/pgo -fprofile-update=atomic "
export LDFLAGS_GENERATE="$LDFLAGS -fprofile-generate -fprofile-dir=/var/tmp/pgo -fprofile-update=atomic "
export CFLAGS_USE="$CFLAGS -fprofile-use -fprofile-dir=/var/tmp/pgo -fprofile-correction "
export FCFLAGS_USE="$FCFLAGS -fprofile-use -fprofile-dir=/var/tmp/pgo -fprofile-correction "
export FFLAGS_USE="$FFLAGS -fprofile-use -fprofile-dir=/var/tmp/pgo -fprofile-correction "
export CXXFLAGS_USE="$CXXFLAGS -fprofile-use -fprofile-dir=/var/tmp/pgo -fprofile-correction "
export LDFLAGS_USE="$LDFLAGS -fprofile-use -fprofile-dir=/var/tmp/pgo -fprofile-correction "
CFLAGS="${CFLAGS_GENERATE}" CXXFLAGS="${CXXFLAGS_GENERATE}" FFLAGS="${FFLAGS_GENERATE}" FCFLAGS="${FCFLAGS_GENERATE}" LDFLAGS="${LDFLAGS_GENERATE}" %configure --disable-static --enable-pcre2-16 \
--enable-pcre2-32 \
--enable-unicode \
--enable-jit=auto
make  %{?_smp_mflags}

make VERBOSE=1 V=1 %{?_smp_mflags} check || :
make clean
CFLAGS="${CFLAGS_USE}" CXXFLAGS="${CXXFLAGS_USE}" FFLAGS="${FFLAGS_USE}" FCFLAGS="${FCFLAGS_USE}" LDFLAGS="${LDFLAGS_USE}" %configure --disable-static --enable-pcre2-16 \
--enable-pcre2-32 \
--enable-unicode \
--enable-jit=auto
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
## build_prepend content
export CFLAGS="$CFLAGS -mshstk"
## build_prepend end
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3"
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3"
%configure --disable-static --enable-pcre2-16 \
--enable-pcre2-32 \
--enable-unicode \
--enable-jit=auto
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../buildavx2;
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1656310256
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pcre2
cp %{_builddir}/pcre2-10.37/LICENCE %{buildroot}/usr/share/package-licenses/pcre2/3005b2c68faac406829c8ea56376ddcb1ed0eabb
cp %{_builddir}/pcre2-10.37/cmake/COPYING-CMAKE-SCRIPTS %{buildroot}/usr/share/package-licenses/pcre2/ff3ed70db4739b3c6747c7f624fe2bad70802987
pushd ../buildavx2/
%make_install_v3
popd
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pcre2-config
/usr/bin/pcre2grep
/usr/bin/pcre2test
/usr/share/clear/optimized-elf/bin*

%files dev
%defattr(-,root,root,-)
/usr/include/pcre2.h
/usr/include/pcre2posix.h
/usr/lib64/glibc-hwcaps/x86-64-v3/libpcre2-16.so
/usr/lib64/glibc-hwcaps/x86-64-v3/libpcre2-32.so
/usr/lib64/glibc-hwcaps/x86-64-v3/libpcre2-8.so
/usr/lib64/glibc-hwcaps/x86-64-v3/libpcre2-posix.so
/usr/lib64/libpcre2-16.so
/usr/lib64/libpcre2-32.so
/usr/lib64/libpcre2-8.so
/usr/lib64/libpcre2-posix.so
/usr/lib64/pkgconfig/libpcre2-16.pc
/usr/lib64/pkgconfig/libpcre2-32.pc
/usr/lib64/pkgconfig/libpcre2-8.pc
/usr/lib64/pkgconfig/libpcre2-posix.pc
/usr/share/man/man3/pcre2.3
/usr/share/man/man3/pcre2_callout_enumerate.3
/usr/share/man/man3/pcre2_code_copy.3
/usr/share/man/man3/pcre2_code_copy_with_tables.3
/usr/share/man/man3/pcre2_code_free.3
/usr/share/man/man3/pcre2_compile.3
/usr/share/man/man3/pcre2_compile_context_copy.3
/usr/share/man/man3/pcre2_compile_context_create.3
/usr/share/man/man3/pcre2_compile_context_free.3
/usr/share/man/man3/pcre2_config.3
/usr/share/man/man3/pcre2_convert_context_copy.3
/usr/share/man/man3/pcre2_convert_context_create.3
/usr/share/man/man3/pcre2_convert_context_free.3
/usr/share/man/man3/pcre2_converted_pattern_free.3
/usr/share/man/man3/pcre2_dfa_match.3
/usr/share/man/man3/pcre2_general_context_copy.3
/usr/share/man/man3/pcre2_general_context_create.3
/usr/share/man/man3/pcre2_general_context_free.3
/usr/share/man/man3/pcre2_get_error_message.3
/usr/share/man/man3/pcre2_get_mark.3
/usr/share/man/man3/pcre2_get_match_data_size.3
/usr/share/man/man3/pcre2_get_ovector_count.3
/usr/share/man/man3/pcre2_get_ovector_pointer.3
/usr/share/man/man3/pcre2_get_startchar.3
/usr/share/man/man3/pcre2_jit_compile.3
/usr/share/man/man3/pcre2_jit_free_unused_memory.3
/usr/share/man/man3/pcre2_jit_match.3
/usr/share/man/man3/pcre2_jit_stack_assign.3
/usr/share/man/man3/pcre2_jit_stack_create.3
/usr/share/man/man3/pcre2_jit_stack_free.3
/usr/share/man/man3/pcre2_maketables.3
/usr/share/man/man3/pcre2_maketables_free.3
/usr/share/man/man3/pcre2_match.3
/usr/share/man/man3/pcre2_match_context_copy.3
/usr/share/man/man3/pcre2_match_context_create.3
/usr/share/man/man3/pcre2_match_context_free.3
/usr/share/man/man3/pcre2_match_data_create.3
/usr/share/man/man3/pcre2_match_data_create_from_pattern.3
/usr/share/man/man3/pcre2_match_data_free.3
/usr/share/man/man3/pcre2_pattern_convert.3
/usr/share/man/man3/pcre2_pattern_info.3
/usr/share/man/man3/pcre2_serialize_decode.3
/usr/share/man/man3/pcre2_serialize_encode.3
/usr/share/man/man3/pcre2_serialize_free.3
/usr/share/man/man3/pcre2_serialize_get_number_of_codes.3
/usr/share/man/man3/pcre2_set_bsr.3
/usr/share/man/man3/pcre2_set_callout.3
/usr/share/man/man3/pcre2_set_character_tables.3
/usr/share/man/man3/pcre2_set_compile_extra_options.3
/usr/share/man/man3/pcre2_set_compile_recursion_guard.3
/usr/share/man/man3/pcre2_set_depth_limit.3
/usr/share/man/man3/pcre2_set_glob_escape.3
/usr/share/man/man3/pcre2_set_glob_separator.3
/usr/share/man/man3/pcre2_set_heap_limit.3
/usr/share/man/man3/pcre2_set_match_limit.3
/usr/share/man/man3/pcre2_set_max_pattern_length.3
/usr/share/man/man3/pcre2_set_newline.3
/usr/share/man/man3/pcre2_set_offset_limit.3
/usr/share/man/man3/pcre2_set_parens_nest_limit.3
/usr/share/man/man3/pcre2_set_recursion_limit.3
/usr/share/man/man3/pcre2_set_recursion_memory_management.3
/usr/share/man/man3/pcre2_set_substitute_callout.3
/usr/share/man/man3/pcre2_substitute.3
/usr/share/man/man3/pcre2_substring_copy_byname.3
/usr/share/man/man3/pcre2_substring_copy_bynumber.3
/usr/share/man/man3/pcre2_substring_free.3
/usr/share/man/man3/pcre2_substring_get_byname.3
/usr/share/man/man3/pcre2_substring_get_bynumber.3
/usr/share/man/man3/pcre2_substring_length_byname.3
/usr/share/man/man3/pcre2_substring_length_bynumber.3
/usr/share/man/man3/pcre2_substring_list_free.3
/usr/share/man/man3/pcre2_substring_list_get.3
/usr/share/man/man3/pcre2_substring_nametable_scan.3
/usr/share/man/man3/pcre2_substring_number_from_name.3
/usr/share/man/man3/pcre2api.3
/usr/share/man/man3/pcre2build.3
/usr/share/man/man3/pcre2callout.3
/usr/share/man/man3/pcre2compat.3
/usr/share/man/man3/pcre2convert.3
/usr/share/man/man3/pcre2demo.3
/usr/share/man/man3/pcre2jit.3
/usr/share/man/man3/pcre2limits.3
/usr/share/man/man3/pcre2matching.3
/usr/share/man/man3/pcre2partial.3
/usr/share/man/man3/pcre2pattern.3
/usr/share/man/man3/pcre2perform.3
/usr/share/man/man3/pcre2posix.3
/usr/share/man/man3/pcre2sample.3
/usr/share/man/man3/pcre2serialize.3
/usr/share/man/man3/pcre2syntax.3
/usr/share/man/man3/pcre2unicode.3

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/pcre2/*

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-pcre2

%files lib
%defattr(-,root,root,-)
/usr/lib64/glibc-hwcaps/x86-64-v3/libpcre2-16.so.0
/usr/lib64/glibc-hwcaps/x86-64-v3/libpcre2-16.so.0.10.2
/usr/lib64/glibc-hwcaps/x86-64-v3/libpcre2-32.so.0
/usr/lib64/glibc-hwcaps/x86-64-v3/libpcre2-32.so.0.10.2
/usr/lib64/glibc-hwcaps/x86-64-v3/libpcre2-8.so.0
/usr/lib64/glibc-hwcaps/x86-64-v3/libpcre2-8.so.0.10.2
/usr/lib64/glibc-hwcaps/x86-64-v3/libpcre2-posix.so.3
/usr/lib64/glibc-hwcaps/x86-64-v3/libpcre2-posix.so.3.0.0
/usr/lib64/libpcre2-16.so.0
/usr/lib64/libpcre2-16.so.0.10.2
/usr/lib64/libpcre2-32.so.0
/usr/lib64/libpcre2-32.so.0.10.2
/usr/lib64/libpcre2-8.so.0
/usr/lib64/libpcre2-8.so.0.10.2
/usr/lib64/libpcre2-posix.so.3
/usr/lib64/libpcre2-posix.so.3.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pcre2/3005b2c68faac406829c8ea56376ddcb1ed0eabb
/usr/share/package-licenses/pcre2/ff3ed70db4739b3c6747c7f624fe2bad70802987

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/pcre2-config.1
/usr/share/man/man1/pcre2grep.1
/usr/share/man/man1/pcre2test.1
