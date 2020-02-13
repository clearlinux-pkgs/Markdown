#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : Markdown
Version  : 3.2.1
Release  : 56
URL      : https://files.pythonhosted.org/packages/98/79/ce6984767cb9478e6818bd0994283db55c423d733cc62a88a3ffb8581e11/Markdown-3.2.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/98/79/ce6984767cb9478e6818bd0994283db55c423d733cc62a88a3ffb8581e11/Markdown-3.2.1.tar.gz
Summary  : A Markdown implementation written in C
Group    : Development/Tools
License  : BSD-3-Clause
Requires: Markdown-bin = %{version}-%{release}
Requires: Markdown-license = %{version}-%{release}
Requires: Markdown-python = %{version}-%{release}
Requires: Markdown-python3 = %{version}-%{release}
Requires: setuptools
BuildRequires : PyYAML
BuildRequires : buildreq-distutils3
BuildRequires : nose
BuildRequires : setuptools

%description
[Python-Markdown][]
===================
[![Build Status][travis-button]][travis]
[![Coverage Status][codecov-button]][codecov]
[![Latest Version][mdversion-button]][md-pypi]
[![Python Versions][pyversion-button]][md-pypi]
[![BSD License][bsdlicense-button]][bsdlicense]
[![Code of Conduct][codeofconduct-button]][Code of Conduct]

%package bin
Summary: bin components for the Markdown package.
Group: Binaries
Requires: Markdown-license = %{version}-%{release}

%description bin
bin components for the Markdown package.


%package license
Summary: license components for the Markdown package.
Group: Default

%description license
license components for the Markdown package.


%package python
Summary: python components for the Markdown package.
Group: Default
Requires: Markdown-python3 = %{version}-%{release}
Provides: markdown-python

%description python
python components for the Markdown package.


%package python3
Summary: python3 components for the Markdown package.
Group: Default
Requires: python3-core

%description python3
python3 components for the Markdown package.


%prep
%setup -q -n Markdown-3.2.1
cd %{_builddir}/Markdown-3.2.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1581561001
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/Markdown
cp %{_builddir}/Markdown-3.2.1/LICENSE.md %{buildroot}/usr/share/package-licenses/Markdown/686030b6b3298c011fe74266f0cde2d2c77f4a13
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/markdown_py

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/Markdown/686030b6b3298c011fe74266f0cde2d2c77f4a13

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
