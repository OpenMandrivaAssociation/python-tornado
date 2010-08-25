%define oname tornado

Name:           python-%{oname}
Version:        1.0.1
Release:        %mkrel 1
Summary:        Scalable, non-blocking web server and tools

Group:          Development/Python
License:        ASL 2.0
URL:            http://www.tornadoweb.org
Source0:        http://github.com/downloads/facebook/tornado/%{oname}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch:      noarch
Requires:       python-pycurl
Requires:       python-simplejson

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
    %{__rm} ${File}.orig
done

# spurious permission fix
find demos/ -name "*.py" -exec chmod -x {} \;

# remove empty file
rm -rf demos/facebook/static/facebook.js

%build
python setup.py build

%install
rm -rf %{buildroot}
python setup.py install --root=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README
%{python_sitelib}/%{oname}/
%{python_sitelib}/%{oname}-%{version}-py%{pyver}.egg-info/

%files doc
%defattr(-,root,root,-)
%doc demos

