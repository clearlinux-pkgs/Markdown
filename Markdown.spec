#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : Markdown
Version  : 2.6.5
Release  : 9
URL      : https://pypi.python.org/packages/source/M/Markdown/Markdown-2.6.5.tar.gz
Source0  : https://pypi.python.org/packages/source/M/Markdown/Markdown-2.6.5.tar.gz
Summary  : Python implementation of Markdown.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: Markdown-bin
Requires: Markdown-python
BuildRequires : PyYAML
BuildRequires : nose
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
[Python-Markdown][]
===================
[![Build Status](http://img.shields.io/travis/waylan/Python-Markdown.svg)](https://travis-ci.org/waylan/Python-Markdown)
[![Coverage Status](https://img.shields.io/coveralls/waylan/Python-Markdown.svg)](https://coveralls.io/r/waylan/Python-Markdown?branch=master)
[![Downloads](http://img.shields.io/pypi/dm/Markdown.svg)](https://pypi.python.org/pypi/Markdown#downloads)
[![Latest Version](http://img.shields.io/pypi/v/Markdown.svg)](http://pypi.python.org/pypi/Markdown)
[![BSD License](http://img.shields.io/badge/license-BSD-yellow.svg)](http://opensource.org/licenses/BSD-3-Clause)

%package bin
Summary: bin components for the Markdown package.
Group: Binaries

%description bin
bin components for the Markdown package.


%package python
Summary: python components for the Markdown package.
Group: Default
Provides: markdown-python

%description python
python components for the Markdown package.


%prep
%setup -q -n Markdown-2.6.5

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python2 run-tests.py
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/markdown_py

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
