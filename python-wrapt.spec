#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define 	module	wrapt
Summary:	A Python module for decorators, wrappers and monkey patching
Name:		python-%{module}
Version:	1.10.5
Release:	3
License:	BSD
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/source/w/wrapt/%{module}-%{version}.tar.gz
# Source0-md5:	79732bbc096235704e7523d3bacd202c
URL:		https://github.com/GrahamDumpleton/wrapt
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-devel
%endif
%if %{with python3}
BuildRequires:	python3-devel
%endif
Requires:	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The aim of the wrapt module is to provide a transparent object proxy
for Python, which can be used as the basis for the construction of
function wrappers and decorator functions.

The wrapt module focuses very much on correctness. It therefore goes
way beyond existing mechanisms such as functools.wraps() to ensure
that decorators preserve introspectability, signatures, type checking
abilities etc. The decorators that can be constructed using this
module will work in far more scenarios than typical decorators and
provide more predictable and consistent behaviour.

%package -n python3-%{module}
Summary:	A Python module for decorators, wrappers and monkey patching
Group:		Libraries/Python
Requires:	python3-modules

%description -n python3-%{module}
The aim of the wrapt module is to provide a transparent object proxy
for Python, which can be used as the basis for the construction of
function wrappers and decorator functions.

The wrapt module focuses very much on correctness. It therefore goes
way beyond existing mechanisms such as functools.wraps() to ensure
that decorators preserve introspectability, signatures, type checking
abilities etc. The decorators that can be constructed using this
module will work in far more scenarios than typical decorators and
provide more predictable and consistent behaviour.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README
%dir %{py_sitedir}/%{module}
%{py_sitedir}/%{module}/*.py[co]
%attr(755,root,root) %{py_sitedir}/%{module}/*.so
%{py_sitedir}/%{module}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc README
%dir %{py3_sitedir}/%{module}
%{py3_sitedir}/%{module}/*.py
%attr(755,root,root) %{py3_sitedir}/%{module}/*.so
%{py3_sitedir}/%{module}/__pycache__
%{py3_sitedir}/%{module}-%{version}-py*.egg-info
%endif
