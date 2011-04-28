%define upstream_name	 Params-Util
%define upstream_version 1.04

Name:		    perl-%{upstream_name}
Version:	    %perl_convert_version %{upstream_version}
Release:	    %mkrel 1

Summary:	    Simple standalone param-checking functions
License:	    GPL+ or Artistic
Group:		    Development/Perl
Url:		    http://search.cpan.org/dist/%{upstream_name}/
Source0:	    http://www.cpan.org/modules/by-module/Params/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:  perl-devel
BuildRoot:	    %{_tmppath}/%{name}-%{version}-%{release}

%description
Params::Util provides a basic set of importable functions that makes checking
parameters a hell of a lot easier.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
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
%{perl_vendorarch}/Params
%{perl_vendorarch}/auto/Params
%{_mandir}/*/*

