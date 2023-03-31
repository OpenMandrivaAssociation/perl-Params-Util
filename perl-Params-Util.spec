%define modname	Params-Util
%define modver	1.102
# broken build system?
%global _debugsource_template %{nil}

Summary:	Simple standalone param-checking functions
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	3
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://metacpan.org/pod/Params::Util
Source0:	http://www.cpan.org/modules/by-module/Params/%{modname}-%{modver}.tar.gz
BuildRequires:	perl-devel
BuildRequires:	perl(Test::More)

%description
Params::Util provides a basic set of importable functions that makes checking
parameters a hell of a lot easier.

%prep
%autosetup -p1 -n %{modname}-%{modver}
chmod 644 Changes lib/Params/Util.pm

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
%make test

%install
%make_install

%files
%doc Changes
%{perl_vendorarch}/Params
%{perl_vendorarch}/auto/Params
%{_mandir}/man3/*
