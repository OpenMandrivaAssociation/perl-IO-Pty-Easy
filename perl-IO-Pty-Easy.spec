%define upstream_name    IO-Pty-Easy
%define upstream_version 0.08

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Easy interface to IO::Pty
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/IO/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(IO::Pty)
BuildRequires: perl(Scalar::Util)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
'IO::Pty::Easy' provides an interface to the IO::Pty manpage which hides
most of the ugly details of handling ptys, wrapping them instead in simple
spawn/read/write commands.

'IO::Pty::Easy' uses the IO::Pty manpage internally, so it inherits all of
the portability restrictions from that module.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes META.yml LICENSE README
%{_mandir}/man3/*
%perl_vendorlib/*


