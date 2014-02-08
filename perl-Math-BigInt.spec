%define	modname	Math-BigInt
%define	modver	1.997

Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	3

Summary:	Arbitrary size integer/float math package
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Math/%{modname}-%{modver}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
All operators (including basic math operations) are overloaded if you declare
your big integers as

  $i = new Math::BigInt '123_456_789_123_456_789';

Operations with overloaded operators preserve the arguments which is exactly
what you expect.

%prep
%setup -q -n %{modname}-%{modver}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files 
%doc README
%{perl_vendorlib}/Math
%{_mandir}/*/*

%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.993.0-5mdv2012.0
+ Revision: 765474
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.993.0-4
+ Revision: 763964
- rebuilt for perl-5.14.x

* Sat May 21 2011 Oden Eriksson <oeriksson@mandriva.com> 1.993.0-3
+ Revision: 676730
- rebuild

* Tue Mar 01 2011 Sandro Cazzaniga <kharec@mandriva.org> 1.993.0-1
+ Revision: 641131
- update to 1.993

* Mon Feb 28 2011 Funda Wang <fwang@mandriva.org> 1.992.0-2
+ Revision: 640770
- rebuild to obsolete old packages

* Sun Feb 20 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.992.0-1
+ Revision: 638918
- update to new version 1.992

* Mon Feb 14 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.991.0-2
+ Revision: 637699
- rebuild to ensure it is loaded before the core module

* Mon Feb 07 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.991.0-1
+ Revision: 636614
- update to new version 1.991

* Tue Nov 16 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.990.0-1mdv2011.0
+ Revision: 598085
- update to new version 1.99

* Sat Nov 13 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.980.0-1mdv2011.0
+ Revision: 597192
- update to 1.98

* Sat Sep 04 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.900.0-1mdv2011.0
+ Revision: 575732
- update to 1.90

* Wed Jul 29 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.890.0-1mdv2011.0
+ Revision: 403851
- rebuild using %%perl_convert_version

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 1.89-2mdv2009.0
+ Revision: 268600
- rebuild early 2009.0 package (before pixel changes)

* Tue Apr 22 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.89-1mdv2009.0
+ Revision: 196478
- update to new version 1.89

* Tue Apr 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.88-1mdv2009.0
+ Revision: 193858
- update to new version 1.88

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Sep 02 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.87-2mdv2008.0
+ Revision: 78149
- noarch package

* Sat Sep 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.87-1mdv2008.0
+ Revision: 77701
- import perl-Math-BigInt


* Thu Aug 31 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.01-6mdv2007.0
- Rebuild

* Thu May 04 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.01-5mdk
- Fix According to perl Policy
    - Source URL
- use mkrel

* Sat Jun 11 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.01-4mdk 
- better url
- spec cleanup
- don't ship useless empty dirs
- make test in %%check

* Mon Dec 20 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.01-3mdk
- fix buildrequires in a backward compatible way

* Fri Jul 23 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.01-2mdk 
- rpmbuildupdate aware

* Mon Jan 05 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.01-1mdk
- first mdk release
