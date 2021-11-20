#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define 	module	wrapt
Summary:	Python 2 module for decorators, wrappers and monkey patching
Summary(pl.UTF-8):	Moduł Pythona 2 do dekorowania, opakowywania i łatania w locie
Name:		python-%{module}
Version:	1.12.1
Release:	3
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/wrapt/
Source0:	https://files.pythonhosted.org/packages/source/w/wrapt/%{module}-%{version}.tar.gz
# Source0-md5:	6d56ed0de4336462a73350341462f45e
URL:		https://github.com/GrahamDumpleton/wrapt
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-devel >= 1:2.7
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.4
%endif
Requires:	python-modules >= 1:2.7
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

%description -l pl.UTF-8
Celem modułu wrapt jest dostarczenie przezroczystego proxy obiektów
dla Pythona. Można go używać jako podstawy do konstruowania opakowań
funkcji lub funkcji dekoratorów.

Moduł wrapt skupia się bardzo na poprawności - wykracza więc poza
istniejące mechanizmy, tkaie jak functools.wraps(), aby zapewnić, że
dekoratory zachowują introspekcje, sygnatury, możliwość sprawdzania
typów itp. Dekoratory tworzone przy użyciu tego modułu będą działać w
większej liczbie scenariuszy niż typowe dekoratory oraz zapewniać
bardziej przewidywalne i spójne zachowanie.

%package -n python3-%{module}
Summary:	Python 3 module for decorators, wrappers and monkey patching
Summary(pl.UTF-8):	Moduł Pythona 3 do dekorowania, opakowywania i łatania w locie
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

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

%description -n python3-%{module} -l pl.UTF-8
Celem modułu wrapt jest dostarczenie przezroczystego proxy obiektów
dla Pythona. Można go używać jako podstawy do konstruowania opakowań
funkcji lub funkcji dekoratorów.

Moduł wrapt skupia się bardzo na poprawności - wykracza więc poza
istniejące mechanizmy, tkaie jak functools.wraps(), aby zapewnić, że
dekoratory zachowują introspekcje, sygnatury, możliwość sprawdzania
typów itp. Dekoratory tworzone przy użyciu tego modułu będą działać w
większej liczbie scenariuszy niż typowe dekoratory oraz zapewniać
bardziej przewidywalne i spójne zachowanie.

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
%doc LICENSE README.rst
%dir %{py_sitedir}/%{module}
%{py_sitedir}/%{module}/*.py[co]
%attr(755,root,root) %{py_sitedir}/%{module}/*.so
%{py_sitedir}/%{module}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc LICENSE README.rst
%dir %{py3_sitedir}/%{module}
%{py3_sitedir}/%{module}/*.py
%attr(755,root,root) %{py3_sitedir}/%{module}/*.so
%{py3_sitedir}/%{module}/__pycache__
%{py3_sitedir}/%{module}-%{version}-py*.egg-info
%endif
