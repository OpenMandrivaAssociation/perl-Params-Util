%define upstream_name	 Params-Util
%define upstream_version 1.07

Name:		    perl-%{upstream_name}
Version:	    %perl_convert_version %{upstream_version}
Release:	    7

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



%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.40.0-4mdv2012.0
+ Revision: 765583
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.40.0-3
+ Revision: 764094
- rebuilt for perl-5.14.x

* Sat May 21 2011 Oden Eriksson <oeriksson@mandriva.com> 1.40.0-2
+ Revision: 676635
- rebuild

* Thu Apr 28 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.40.0-1
+ Revision: 659981
- update to new version 1.04

* Sun Nov 28 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.30.0-1mdv2011.0
+ Revision: 602385
- update to new version 1.03

* Tue Jul 20 2010 J茅r么me Quelin <jquelin@mandriva.org> 1.10.0-3mdv2011.0
+ Revision: 556068
- rebuild for perl 5.12

* Tue Jul 20 2010 J茅r么me Quelin <jquelin@mandriva.org> 1.10.0-2mdv2011.0
+ Revision: 555655
- rebuild

* Mon Mar 22 2010 J茅r么me Quelin <jquelin@mandriva.org> 1.10.0-1mdv2010.1
+ Revision: 526453
- update to 1.01

* Thu Jul 16 2009 J茅r么me Quelin <jquelin@mandriva.org> 1.0.0-1mdv2010.0
+ Revision: 396614
- rebuilding to take new automatic provides extraction into account
- using %%perl_convert_version
- fixed license field

* Sun Jun 07 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.00-1mdv2010.0
+ Revision: 383533
- update to new version 1.00

* Wed Feb 18 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.38-1mdv2009.1
+ Revision: 342397
- update to new version 0.38

* Fri Feb 06 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.37-1mdv2009.1
+ Revision: 338017
- update to new version 0.37

* Sat Jan 31 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.36-1mdv2009.1
+ Revision: 335891
- update to new version 0.36

* Thu Nov 13 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.35-1mdv2009.1
+ Revision: 302812
- new version

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.33-2mdv2009.0
+ Revision: 268707
- rebuild early 2009.0 package (before pixel changes)

* Wed May 28 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.33-1mdv2009.0
+ Revision: 212217
- update to new version 0.33

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Nov 17 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.31-1mdv2008.1
+ Revision: 109578
- update to new version 0.31

* Tue Oct 23 2007 Funda Wang <fwang@mandriva.org> 0.30-1mdv2008.1
+ Revision: 101542
- update to new version 0.30

* Thu Aug 30 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.29-1mdv2008.0
+ Revision: 75229
- update to new version 0.29

* Wed Aug 22 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.28-1mdv2008.0
+ Revision: 69244
- update to new version 0.28

* Wed Aug 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.26-1mdv2008.0
+ Revision: 63961
- update to new version 0.26

* Sun Jul 01 2007 Olivier Thauvin <nanardon@mandriva.org> 0.25-1mdv2008.0
+ Revision: 46225
- 0.25


* Sat Mar 03 2007 Olivier Thauvin <nanardon@mandriva.org> 0.23-1mdv2007.0
+ Revision: 131712
- 0.23

* Wed Dec 13 2006 Olivier Thauvin <nanardon@mandriva.org> 0.22-1mdv2007.1
+ Revision: 96131
- 0.22
- Import perl-Params-Util

* Wed Aug 30 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.17-1mdv2007.0
- New version 0.17

* Mon Jul 10 2006 Emmanuel Andry <eandry@mandriva.org> 0.15-1mdv2007.0
- New release 0.15

* Tue May 30 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.14-1mdv2007.0
- New release 0.14

* Fri May 05 2006 Nicolas L閏ureuil <neoclust@mandriva.org> 0.12-1mdk
- New release 0.12
- Fix typo on Source URL

* Sun Apr 16 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.11-1mdk
- New release 0.11
- better source URL

* Fri Feb 03 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.10-1mdk
- 0.10

* Tue Jan 10 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.09-1mdk
- 0.09

* Tue Oct 11 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.07-1mdk
- 0.07

* Fri Oct 07 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.06-1mdk
- new version  
- %%mkrel
- spec cleanup
- fix directory ownership
- rpmbuildupdate aware

* Sat Aug 20 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.05-1mdk
- Initial MDV release.

