%define oname tornado
%define debug_package %{nil}

Name:           python-%{oname}
Version:	6.0.4
Release:	1
Summary:        Scalable, non-blocking web server and tools
Group:          Development/Python
License:        ASL 2.0
URL:            http://www.tornadoweb.org
Source0:	https://files.pythonhosted.org/packages/95/84/119a46d494f008969bf0c775cb2c6b3579d3c4cc1bb1b41a022aa93ee242/tornado-6.0.4.tar.gz
Source1:        %{name}.rpmlintrc
BuildRequires:	python-devel
Requires:	    python
Requires:       python-pycurl

%description
Tornado is an open source version of the scalable, non-blocking web server and
and tools.

The framework is distinct from most mainstream web server frameworks (and
certainly most Python frameworks) because it is non-blocking and reasonably
fast. Because it is non-blocking and uses epoll, it can handle thousands of
simultaneous standing connections, which means it is ideal for real-time web
services.

%package doc
Summary:        Examples for python-tornado
Group:          Development/Python
Requires:       %{name} = %{version}-%{release}

%description doc
Tornado is an open source version of the scalable, non-blocking web server and
and tools. This package contains some example applications.

%prep 
%setup -q -n %{oname}-%{version}

# remove shebang from files
%{__sed} -i.orig -e '/^#!\//, 1d' *py tornado/*.py tornado/*/*.py

# spurious permission fix
find demos/ -name "*.py" -exec chmod -x {} \;

# remove empty file
rm -rf demos/facebook/static/facebook.js

%build
python setup.py build

%install
python setup.py install --root=%{buildroot}

%files
%doc 
%{py_platsitedir}/%{oname}/
%{py_platsitedir}/%{oname}-%{version}-py%{py_ver}.egg-info

%files doc
%doc demos
