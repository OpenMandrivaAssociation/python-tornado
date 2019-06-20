%define oname tornado
%define debug_package %{nil}

Name:           python-%{oname}
Version:	6.0.2
Release:        2
Summary:        Scalable, non-blocking web server and tools
Group:          Development/Python
License:        ASL 2.0
URL:            http://www.tornadoweb.org
Source0:        https://pypi.python.org/packages/source/t/tornado/tornado-%{version}.tar.gz
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
%{py_platsitedir}/%{oname}-%{version}-py%{py_ver}.egg-info/

%files doc
%doc demos
