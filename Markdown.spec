#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : Markdown
Version  : 2.6.11
Release  : 35
URL      : http://pypi.debian.net/Markdown/Markdown-2.6.11.tar.gz
Source0  : http://pypi.debian.net/Markdown/Markdown-2.6.11.tar.gz
Summary  : Python implementation of Markdown.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: Markdown-bin
Requires: Markdown-python3
Requires: Markdown-python
BuildRequires : PyYAML
BuildRequires : PyYAML-legacypython
BuildRequires : nose
BuildRequires : nose-legacypython
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
This is a Python implementation of John Gruber's Markdown_.
        It is almost completely compliant with the reference implementation,
        though there are a few known issues. See Features_ for information
        on what exactly is supported and what is not. Additional features are
        supported by the `Available Extensions`_.

%package bin
Summary: bin components for the Markdown package.
Group: Binaries

%description bin
bin components for the Markdown package.


%package legacypython
Summary: legacypython components for the Markdown package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the Markdown package.


%package python
Summary: python components for the Markdown package.
Group: Default
Requires: Markdown-python3
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
%setup -q -n Markdown-2.6.11

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1526001909
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python2 run-tests.py
%install
export SOURCE_DATE_EPOCH=1526001909
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/markdown_py

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
