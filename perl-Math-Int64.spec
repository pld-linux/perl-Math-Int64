#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define		pdir	Math
%define		pnam	Int64
Summary:	Math::Int64 - Manipulate 64 bits integers in Perl
Summary(pl.UTF-8):	Math::Int64 - operowanie na 64-bitowych liczbach całkowitych w Perlu
Name:		perl-Math-Int64
Version:	0.57
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-module/Math/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ed431cca1c403b1078fb1b3e2860d8de
URL:		https://metacpan.org/dist/Math-Int64
BuildRequires:	perl-ExtUtils-MakeMaker
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl(blib) >= 1.01
BuildRequires:	perl-Storable
BuildRequires:	perl-Test-Simple >= 0.96
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module adds support for 64 bit integers, signed and unsigned, to
Perl.

%description -l pl.UTF-8
Ten moduł dodaje do Perla obsługę 64-bitowych liczb całkowitych -
zarówno ze znakiem, jak i bez.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README.md
%{perl_vendorarch}/Math/Int64.pm
%{perl_vendorarch}/Math/Int64
%{perl_vendorarch}/Math/UInt64.pm
%dir %{perl_vendorarch}/auto/Math/Int64
%attr(755,root,root) %{perl_vendorarch}/auto/Math/Int64/Int64.so
%{_mandir}/man3/Math::Int64.3pm*
%{_mandir}/man3/Math::Int64::*.3pm*
%{_mandir}/man3/Math::UInt64.3pm*
%{_examplesdir}/%{name}-%{version}
