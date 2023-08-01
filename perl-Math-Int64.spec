#
# Conditional build:
%bcond_without	tests		# unit tests
#
%define		pdir	Math
%define		pnam	Int64
Summary:	Math::Int64 - Manipulate 64 bits integers in Perl
Name:		perl-Math-Int64
Version:	0.54
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Math/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1ad0ce8b5e903dfe9f7ffbabd8a43014
URL:		https://metacpan.org/dist/Math-Int64
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module adds support for 64 bit integers, signed and unsigned, to
Perl.

The lexical pragma Math::Int64::die_on_overflow configures the module
to throw an error when some operation results in integer overflow.

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
%doc Changes INSTALL
%{perl_vendorarch}/Math/*.pm
%{perl_vendorarch}/Math/Int64
%dir %{perl_vendorarch}/auto/Math/Int64
%attr(755,root,root) %{perl_vendorarch}/auto/Math/Int64/*.so
%{_mandir}/man3/Math::*Int64*
%{_examplesdir}/%{name}-%{version}
