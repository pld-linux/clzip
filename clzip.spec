Summary:	LZMA file compressor (C implementation)
Summary(pl.UTF-8):	Kompresor plików oparty na algorytmie LZMA (implementacja w C)
Name:		clzip
Version:	1.13
Release:	1
License:	GPL v3+
Group:		Applications/Archiving
Source0:	http://download.savannah.gnu.org/releases/lzip/clzip/%{name}-%{version}.tar.lz
# Source0-md5:	cef8d6391f2e5758e64835b236a4a60b
Patch0:		%{name}-info.patch
URL:		http://savannah.nongnu.org/projects/lzip/
BuildRequires:	lzip
BuildRequires:	tar >= 1:1.22
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lzip is a lossless file compressor based on the LZMA
(Lempel-Ziv-Markov chain-Algorithm) algorithm designed by Igor Pavlov.
Clzip is in fact a C language version of lzip, intended for embedded
devices or systems lacking a C++ compiler.

%description -l pl.UTF-8
Lzip to bezstratny kompresor plików oparty na algorytmie LZMA
(Lempel-Ziv-Markov chain-Algorithm) opracowanym przez Igora Pawłowa.
Clzip to wersja lzipa napisana w języku C, przeznaczona głównie dla
systemów wbudowanych lub nie mających kompilatora C++.

%prep
%setup -q
%patch0 -p1

%build
%configure
%{__make} all info

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/clzip
%{_mandir}/man1/clzip.1*
%{_infodir}/clzip.info*
