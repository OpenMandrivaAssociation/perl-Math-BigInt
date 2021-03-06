%define	modname	Math-BigInt
%define modver 1.999818

Summary:	Arbitrary size integer/float math package

Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Math/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRequires:	perl-Module-Install
BuildRequires:	perl-Test-Simple

%description
All operators (including basic math operations) are overloaded if you declare
your big integers as

  $i = new Math::BigInt '123_456_789_123_456_789';

Operations with overloaded operators preserve the arguments which is exactly
what you expect.

%prep
%setup -qn %{modname}-%{modver}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
%make_build test

%install
%makeinstall_std

%files 
%doc README
%{perl_vendorlib}/Math
%{_mandir}/man3/*


