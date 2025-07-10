#
# Conditional build:
%bcond_without	tests	# unit tests

%define 	module	wrapt
Summary:	Python module for decorators, wrappers and monkey patching
Summary(pl.UTF-8):	Moduł Pythona do dekorowania, opakowywania i łatania w locie
Name:		python3-%{module}
Version:	1.17.2
Release:	1
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/wrapt/
Source0:	https://files.pythonhosted.org/packages/source/w/wrapt/%{module}-%{version}.tar.gz
# Source0-md5:	f4db93e73e5c70a59955f0ec162d585d
URL:		https://github.com/GrahamDumpleton/wrapt
BuildRequires:	python3-devel >= 1:3.8
BuildRequires:	python3-setuptools >= 1:38.3.0
%if %{with tests}
BuildRequires:	python3-pytest
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.8
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

%prep
%setup -q -n %{module}-%{version}

%build
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTHONPATH=$(echo $(pwd)/build-3/lib.*) \
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%dir %{py3_sitedir}/%{module}
%{py3_sitedir}/%{module}/*.py
%attr(755,root,root) %{py3_sitedir}/%{module}/*.so
%{py3_sitedir}/%{module}/__pycache__
%{py3_sitedir}/%{module}-%{version}-py*.egg-info
