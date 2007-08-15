%define module	Params-Util
%define name	perl-%{module}
%define version	0.26
%define	release	%mkrel 1

Name:		    %{name}
Version:	    %{version}
Release:	    %{release}
Summary:	    Simple standalone param-checking functions
License:	    GPL or Artistic
Group:		    Development/Perl
Url:		    http://search.cpan.org/dist/%{module}/
Source:		    http://www.cpan.org/modules/by-module/Params/%{module}-%{version}.tar.gz
%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif
BuildArch:	    noarch
BuildRoot:	    %{_tmppath}/%{name}-%{version}

%description
Params::Util provides a basic set of importable functions that makes checking
parameters a hell of a lot easier.

%prep
%setup -q -n %{module}-%{version}
chmod 644 Changes README lib/Params/Util.pm

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Params
%{_mandir}/*/*


