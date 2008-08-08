%define module  Math-BigInt
%define name    perl-%{module}
%define version 1.89
%define release %mkrel 2

Name:       %{name}
Version:    %{version}
Release:    %{release}
Summary:    Arbitrary size integer/float math package
License:    GPL or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/Math/%{module}-%{version}.tar.gz
BuildArch:  noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
All operators (including basic math operations) are overloaded if you declare
your big integers as

  $i = new Math::BigInt '123_456_789_123_456_789';

Operations with overloaded operators preserve the arguments which is exactly
what you expect.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc README
%{perl_vendorlib}/Math
%{_mandir}/*/*

