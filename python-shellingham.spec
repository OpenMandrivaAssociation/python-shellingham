Summary:	A tool to Detect Surrounding Shell
Name:		python-shellingham
Version:	1.5.4
Release:	1
License:	ISC
Group:		Development/Python
URL:		https://pypi.org/project/shellingham/
Source0:	https://files.pythonhosted.org/packages/source/s/shellingham/shellingham-%{version}.tar.gz
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

BuildArch:	noarch

%description
Shellingham detects what shell the current Python executable is running in.

%files
%license LICENSE
%doc README.rst
%{py_sitedir}/shellingham
%{py_sitedir}/shellingham-*.*-info

#--------------------------------------------------------------------

%prep
%autosetup -p1 -n shellingham-%{version}

%build
%py_build

%install
%py_install

