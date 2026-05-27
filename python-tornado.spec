%define module tornado
%bcond tests 1

Name:		python-tornado
Version:	6.5.6
Release:	1
Summary:	Scalable, non-blocking web server and tools
Group:		Development/Python
License:	Apache-2.0
URL:		https://www.tornadoweb.org
Source0:	https://github.com/tornadoweb/tornado/archive/v%{version}/%{name}-%{version}.tar.gz
Source100:	%{name}.rpmlintrc

BuildSystem: python
BuildRequires:	fdupes
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
%if %{with tests}
BuildRequires:	python%{pyver}dist(mock)
BuildRequires:	python%{pyver}dist(pycurl)
BuildRequires:	python%{pyver}dist(twisted)
%endif

%description
Tornado is an open source version of the scalable, non-blocking web server and
and tools.

The framework is distinct from most mainstream web server frameworks (and
certainly most Python frameworks) because it is non-blocking and reasonably
fast. Because it is non-blocking and uses epoll, it can handle thousands of
simultaneous standing connections, which means it is ideal for real-time web
services.

%package doc
Summary:	Examples for python-tornado
Group:		Development/Python
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description doc
Tornado is an open source version of the scalable, non-blocking web server and
and tools. This package contains some example applications.

%prep -a
# Remove bundled egg-info
rm -rf %{module}.egg-info

# Fix non-executable script rpmlint issue:
find tornado -name "*.py" -exec sed -i "/#\!\/usr\/bin\/.*/d" {} \;

%build -p
export LDFLAGS="%{ldflags} -lpython%{pyver}"

%install -a
# Do not install tests
rm -rf %{buildroot}%{python_sitearch}/%{module}/test
# Deduplicate module
%fdupes %{buildroot}%{python_sitearch}

# Install demos into _docdir and deduplicate
mkdir -p %{buildroot}%{_docdir}/%{name}
cp -rp demos %{buildroot}%{_docdir}/%{name}
# Fix shebangs
find %{buildroot}%{_docdir}/%{name} -name "*.py" -exec sed -i '1s|^#!.*$|#!%{__python}|' {} \;
# Ensure demo files are not executable
find %{buildroot}%{_docdir}/%{name} -type f -exec chmod a-x {} \;
# Deduplicate docdir contents
%fdupes %{buildroot}%{_docdir}/%{name}

%if %{with tests}
%check
export CI=true
export PYTHONPATH="%{buildroot}%{python_sitearch}:$PWD"
# Skip the same timing-related tests that upstream skips when run in Travis CI.
# https://github.com/tornadoweb/tornado/commit/abc5780a06a1edd0177a399a4dd4f39497cb0c57
export TRAVIS=true
# Increase timeout for tests on riscv64
%ifarch riscv64
	export ASYNC_TEST_TIMEOUT=80
%else
	export ASYNC_TEST_TIMEOUT=30
%endif
%{__python} -m tornado.test
%endif

%files
%doc README.rst
%doc %{_docdir}/%{name}/demos
%{python_sitearch}/%{module}
%{python_sitearch}/%{module}-%{version}.dist-info

