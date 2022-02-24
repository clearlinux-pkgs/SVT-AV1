#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : SVT-AV1
Version  : 0.9.1
Release  : 11
URL      : https://gitlab.com/AOMediaCodec/SVT-AV1/-/archive/v0.9.1/SVT-AV1-v0.9.1.tar.gz
Source0  : https://gitlab.com/AOMediaCodec/SVT-AV1/-/archive/v0.9.1/SVT-AV1-v0.9.1.tar.gz
Summary  : AV1-compliant encoder library core.
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause BSD-3-Clause-Clear MIT
Requires: SVT-AV1-bin = %{version}-%{release}
Requires: SVT-AV1-lib = %{version}-%{release}
Requires: SVT-AV1-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-meson
BuildRequires : git
BuildRequires : glibc-dev
BuildRequires : nasm-bin
BuildRequires : pkg-config
BuildRequires : pkgconfig(gstreamer-1.0)
BuildRequires : pkgconfig(gstreamer-base-1.0)
BuildRequires : pkgconfig(gstreamer-video-1.0)
BuildRequires : python3

%description
# Scalable Video Technology for AV1 (SVT-AV1 Encoder and Decoder)
The Scalable Video Technology for AV1 (SVT-AV1 Encoder and Decoder) is an AV1-compliant encoder/decoder library core. The SVT-AV1 encoder development is a work-in-progress targeting performance levels applicable to both VOD and Live encoding / transcoding video applications. The SVT-AV1 decoder implementation is targeting future codec research activities.

%package bin
Summary: bin components for the SVT-AV1 package.
Group: Binaries
Requires: SVT-AV1-license = %{version}-%{release}

%description bin
bin components for the SVT-AV1 package.


%package dev
Summary: dev components for the SVT-AV1 package.
Group: Development
Requires: SVT-AV1-lib = %{version}-%{release}
Requires: SVT-AV1-bin = %{version}-%{release}
Provides: SVT-AV1-devel = %{version}-%{release}
Requires: SVT-AV1 = %{version}-%{release}

%description dev
dev components for the SVT-AV1 package.


%package lib
Summary: lib components for the SVT-AV1 package.
Group: Libraries
Requires: SVT-AV1-license = %{version}-%{release}

%description lib
lib components for the SVT-AV1 package.


%package license
Summary: license components for the SVT-AV1 package.
Group: Default

%description license
license components for the SVT-AV1 package.


%prep
%setup -q -n SVT-AV1-v0.9.1
cd %{_builddir}/SVT-AV1-v0.9.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1645722462
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1645722462
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/SVT-AV1
cp %{_builddir}/SVT-AV1-v0.9.1/LICENSE-BSD2.md %{buildroot}/usr/share/package-licenses/SVT-AV1/3a6355145854d7b1eab7a96b586b49b1f3925041
cp %{_builddir}/SVT-AV1-v0.9.1/LICENSE.md %{buildroot}/usr/share/package-licenses/SVT-AV1/46e7694aaf9130a640379739ddc0b972f98a7230
cp %{_builddir}/SVT-AV1-v0.9.1/third_party/cpuinfo/LICENSE %{buildroot}/usr/share/package-licenses/SVT-AV1/3e10e8cc50f6524daf4c62cc0daae3ccd187da3e
cp %{_builddir}/SVT-AV1-v0.9.1/third_party/cpuinfo/deps/clog/LICENSE %{buildroot}/usr/share/package-licenses/SVT-AV1/aef1ae9e4471bbac8a19a56ae105e87602ab02bc
cp %{_builddir}/SVT-AV1-v0.9.1/third_party/fastfeat/LICENSE %{buildroot}/usr/share/package-licenses/SVT-AV1/7cbe19df00ff13a33eb7638354c37c4f7382f94f
cp %{_builddir}/SVT-AV1-v0.9.1/third_party/googletest/LICENSE %{buildroot}/usr/share/package-licenses/SVT-AV1/5a2314153eadadc69258a9429104cd11804ea304
cp %{_builddir}/SVT-AV1-v0.9.1/third_party/safestringlib/LICENSE %{buildroot}/usr/share/package-licenses/SVT-AV1/4902cae9d3ebedcfbd51da29a80c5eba5c7e308a
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/SvtAv1DecApp
/usr/bin/SvtAv1EncApp

%files dev
%defattr(-,root,root,-)
/usr/include/svt-av1/EbDebugMacros.h
/usr/include/svt-av1/EbSvtAv1.h
/usr/include/svt-av1/EbSvtAv1Dec.h
/usr/include/svt-av1/EbSvtAv1Enc.h
/usr/include/svt-av1/EbSvtAv1ErrorCodes.h
/usr/include/svt-av1/EbSvtAv1ExtFrameBuf.h
/usr/include/svt-av1/EbSvtAv1Formats.h
/usr/include/svt-av1/EbSvtAv1Metadata.h
/usr/lib64/libSvtAv1Dec.so
/usr/lib64/libSvtAv1Enc.so
/usr/lib64/pkgconfig/SvtAv1Dec.pc
/usr/lib64/pkgconfig/SvtAv1Enc.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libSvtAv1Dec.so.0
/usr/lib64/libSvtAv1Dec.so.0.8.7
/usr/lib64/libSvtAv1Enc.so.0
/usr/lib64/libSvtAv1Enc.so.0.9.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/SVT-AV1/3a6355145854d7b1eab7a96b586b49b1f3925041
/usr/share/package-licenses/SVT-AV1/3e10e8cc50f6524daf4c62cc0daae3ccd187da3e
/usr/share/package-licenses/SVT-AV1/46e7694aaf9130a640379739ddc0b972f98a7230
/usr/share/package-licenses/SVT-AV1/4902cae9d3ebedcfbd51da29a80c5eba5c7e308a
/usr/share/package-licenses/SVT-AV1/5a2314153eadadc69258a9429104cd11804ea304
/usr/share/package-licenses/SVT-AV1/7cbe19df00ff13a33eb7638354c37c4f7382f94f
/usr/share/package-licenses/SVT-AV1/aef1ae9e4471bbac8a19a56ae105e87602ab02bc
