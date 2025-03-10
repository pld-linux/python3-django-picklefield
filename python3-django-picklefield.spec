#
# Conditional build:
%bcond_with	tests	# unit tests (not included in sdist)

%define 	module	django-picklefield
Summary:	Pickled object field for Django
Summary(pl.UTF-8):	Serializowalne przez pickle pole obiektowe dla Django
Name:		python3-%{module}
# keep as compatible with python3-django.spec version (3.0.x support Django 2.2/3.0, 3.1.x supports Django 3.2/4.0)
Version:	3.0.1
Release:	2
License:	MIT
Group:		Development/Languages/Python
Source0:	https://files.pythonhosted.org/packages/source/d/django-picklefield/%{module}-%{version}.tar.gz
# Source0-md5:	cedb9a5ba937b6d9a5b78989e81885ac
URL:		https://pypi.org/project/django-picklefield/
BuildRequires:	python3-devel >= 1:3.5
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-django >= 2.2
%endif
BuildRequires:	rpmbuild(macros) >= 1.714
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
django-picklefield provides an implementation of a pickled object
field. Such fields can contain any picklable objects.

%description -l pl.UTF-8
django-picklefield dostarcza implementację pola obiektowego
serializowalnego przez pickle. Pola takie mogą zawierać dowolne
serializowalne obiekty.

%prep
%setup -q -n %{module}-%{version}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/picklefield
%{py3_sitescriptdir}/django_picklefield-%{version}-*.egg-info
