%define oname tornado

Name:           python-%{oname}
Version:        3.2
Release:        1
Summary:        Scalable, non-blocking web server and tools

Group:          Development/Python
License:        ASL 2.0
URL:            http://www.tornadoweb.org
Source0:        https://pypi.python.org/packages/source/t/tornado/tornado-%{version}.tar.gz
Source1:	%{name}.rpmlintrc
BuildArch:      noarch
BuildRequires:	python-devel
Requires:	python
Requires:       python-pycurl
Requires:       python-simplejson
# no matter what cannot remove dependency on it, and then does not
# generate the provides...
Provides:	pythonegg(tornado)

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
for File in `find %{oname} -name "*py"`; do
    %{__sed} -i.orig -e 1d ${File}
    touch -r ${File}.orig ${File}
    rm ${File}.orig
done

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
%{py_puresitedir}/%{oname}/
%{py_puresitedir}/%{oname}-%{version}-py%{py_ver}.egg-info/
%{_libdir}/debug/.build-id/37/550b52c9128000a6ac52d6de4c8896ce30b6de
%{_libdir}/debug/.build-id/37/550b52c9128000a6ac52d6de4c8896ce30b6de.debug
%{_libdir}/debug%{py_puresitedir}/tornado/speedups.so.debug
/usr/src/debug/tornado-3.2/tornado/speedups.c

%files doc
%doc demos



