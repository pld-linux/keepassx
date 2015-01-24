# TODO
# - forcing our cflags breaks build
%define pre alpha6
%define	rel 1
Summary:	KeePassX - Cross Platform Password Manager
Summary(pl.UTF-8):	KeePassX - Wieloplatformowy zarządca haseł
Name:		keepassx
Version:	2.0
Release:	0.%{pre}.%{rel}
License:	GPL v2+
Group:		X11/Applications
#Source0:	http://downloads.sourceforge.net/keepassx/keepassx-%{version}.tar.gz
Source0:	http://www.keepassx.org/dev/attachments/download/69/%{name}-%{version}-%{pre}.tar.gz
# Source0-md5:	7c1c3a42aff63abd8db3bc8df6c963f6
Patch0:		git.patch
URL:		http://keepassx.sourceforge.net/
BuildRequires:	QtCore-devel >= 4.6.0
BuildRequires:	QtDBus-devel >= 4.6.0
BuildRequires:	QtGui-devel >= 4.6.0
BuildRequires:	QtXml-devel >= 4.6.0
BuildRequires:	libgcrypt-devel >= 1.6
BuildRequires:	qt4-build >= 4.6.0
BuildRequires:	qt4-linguist >= 4.6.0
BuildRequires:	qt4-qmake >= 4.6.0
BuildRequires:	rpmbuild(macros) >= 1.230
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXtst-devel
BuildRequires:	zlib-devel
Requires:	desktop-file-utils
Requires:	hicolor-icon-theme
Requires:	shared-mime-info
Obsoletes:	KeePassX
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KeePassX is a free/open-source password manager or safe which helps
you to manage your passwords in a secure way. You can put all your
passwords in one database, which is locked with one master key or a
key-disk. So you only have to remember one single master password or
insert the key-disk to unlock the whole database. The databases are
encrypted using the best and most secure encryption algorithms
currently known (AES and Twofish).

%description -l pl.UTF-8
KeePassX to darmowy i mający otwarte źródła zarządca do przechowywania
haseł, który pozwala na zarządzanie hasłami w bardzo bezpieczny
sposób. Pozwala umieścić wszystkie swoje hasła w jednej bazie, która
jest zabezpieczona poprzez jedno bardzo trudne hasło albo dysk z
kluczem. Wystarczy więc zapamiętać jedno trudne hasło lub umieścić
dysk z kluczem aby odblokować całą bazę z kluczami. Baza jest
zaszyfrowana najlepszymi i najbardziej bezpiecznymi algorytmami
szyfrowania jakie są do tej pory znane (AES i TwoFish).

%prep
%setup -q -n %{name}-%{version}-%{pre}
%patch0 -p1

%build
install -d build
cd build
%cmake \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
%update_desktop_database
%update_mime_database

%postun
%update_icon_cache hicolor
%update_desktop_database_postun
%update_mime_database

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/keepassx
%{_datadir}/mime/packages/keepassx.xml
%{_desktopdir}/keepassx.desktop
%dir %{_datadir}/keepassx
%{_datadir}/keepassx/icons
%dir %{_datadir}/keepassx/translations
%lang(de) %{_datadir}/keepassx/translations/keepassx_de.qm
%{_datadir}/keepassx/translations/keepassx_en_plurals.qm
%lang(it) %{_datadir}/keepassx/translations/keepassx_it.qm
%lang(nl) %{_datadir}/keepassx/translations/keepassx_nl_NL.qm
%lang(sv) %{_datadir}/keepassx/translations/keepassx_sv.qm
%dir %{_libdir}/keepassx
%attr(755,root,root) %{_libdir}/keepassx/libkeepassx-autotype-x11.so
%{_iconsdir}/hicolor/*x*/apps/keepassx.png
%{_iconsdir}/hicolor/*x*/mimetypes/application-x-keepassx.png
%{_iconsdir}/hicolor/scalable/apps/keepassx.svgz