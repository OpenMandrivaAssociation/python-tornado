%define oname tornado

Name:           python-%{oname}
Version:        3.1
Release:        2
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
    %{__rm} ${File}.orig
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

%files doc
%doc demos


%changelog
* Fri Jun 24 2011 Jani Välimaa <wally@mandriva.org> 2.0-1mdv2011.0
+ Revision: 686971
- new version 2.0

* Fri Mar 04 2011 Jani Välimaa <wally@mandriva.org> 1.2.1-1
+ Revision: 641623
- new version 1.2.1

* Mon Feb 21 2011 Jani Välimaa <wally@mandriva.org> 1.2-1
+ Revision: 639184
- new version 1.2

* Fri Feb 11 2011 Jani Välimaa <wally@mandriva.org> 1.1.1-1
+ Revision: 637291
- new version 1.1.1
- drop obsolete py_requires macro

* Sat Oct 30 2010 Michael Scherer <misc@mandriva.org> 1.1-2mdv2011.0
+ Revision: 590591
- rebuild for python 2.7

* Wed Sep 08 2010 Jani Välimaa <wally@mandriva.org> 1.1-1mdv2011.0
+ Revision: 576796
- new version 1.1

* Wed Aug 25 2010 Jani Välimaa <wally@mandriva.org> 1.0.1-1mdv2011.0
+ Revision: 573152
- add python requires
- initial mdv release based on Fedora .spec


