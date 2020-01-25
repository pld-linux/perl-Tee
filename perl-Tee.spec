#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	Tee
Summary:	Tee - Pure Perl emulation of GNU tee
#Summary(pl.UTF-8):	
Name:		perl-Tee
Version:	0.14
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/D/DA/DAGOLDEN/Tee-%{version}.tar.gz
# Source0-md5:	5c189150962550b0348c31f6f3e6ad62
URL:		http://search.cpan.org/dist/Tee/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Probe::Perl)
BuildRequires:	perl-IO-CaptureOutput
BuildRequires:	perl-IPC-Run3 >= 0.033
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Tee distribution provides the ptee program, a pure Perl emulation
of the standard GNU tool tee.  It is designed to be a
platform-independent replacement for operating systems without a
native tee program. As with tee, it passes input received on STDIN
through to STDOUT while also writing a copy of the input to one or
more files.  By default, files will be overwritten.

# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{version}

%build
%{__perl} Makefile.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%attr(755,root,root) %{_bindir}/*
%{perl_vendorlib}/*.pm
%{perl_vendorlib}/Tee
%{_mandir}/man?/*
