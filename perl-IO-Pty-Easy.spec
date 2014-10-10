%define upstream_name    IO-Pty-Easy
%define upstream_version 0.09

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 0.09
Release:	2

Summary:	Easy interface to IO::Pty
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/IO/IO-Pty-Easy-0.09.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(IO::Pty)
BuildRequires:	perl(Scalar::Util)
BuildArch:	noarch

%description
'IO::Pty::Easy' provides an interface to the IO::Pty manpage which hides
most of the ugly details of handling ptys, wrapping them instead in simple
spawn/read/write commands.

'IO::Pty::Easy' uses the IO::Pty manpage internally, so it inherits all of
the portability restrictions from that module.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.80.0-2mdv2011.0
+ Revision: 655033
- rebuild for updated spec-helper

* Fri Mar 05 2010 Jérôme Quelin <jquelin@mandriva.org> 0.80.0-1mdv2011.0
+ Revision: 514790
- import perl-IO-Pty-Easy


* Fri Mar 05 2010 cpan2dist 0.08-1mdv
- initial mdv release, generated with cpan2dist

