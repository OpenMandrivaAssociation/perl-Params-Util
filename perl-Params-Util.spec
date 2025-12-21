%define modname	Params-Util

Summary:	Simple standalone param-checking functions
Name:		perl-%{modname}
Version:	1.102
Release:	6
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/pod/Params::Util
Source0:	http://www.cpan.org/modules/by-module/Params/%{modname}-%{version}.tar.gz
BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Test::More)

%description
Params::Util provides a basic set of importable functions that makes checking
parameters a hell of a lot easier.

%prep
%autosetup -p1 -n %{modname}-%{version}
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
