Summary:	KeePassX - Cross Platform Password Manager
Summary(pl.UTF-8):	KeePassX - Wieloplatformowy zarządca haseł
Name:		keepassx
Version:	2.0.2
Release:	2
License:	GPL v2+
Group:		X11/Applications
Source0:	http://www.keepassx.org/releases/%{version}/keepassx-%{version}.tar.gz
# Source0-md5:	65d098dff663768911847a1e92d0f01d
Patch0:		git.patch
URL:		https://www.keepassx.org/
BuildRequires:	Qt5Concurrent-devel >= 5.2.0
BuildRequires:	Qt5Core-devel >= 5.2.0
BuildRequires:	Qt5Test-devel >= 5.2.0
BuildRequires:	Qt5Widgets-devel >= 5.2.0
BuildRequires:	Qt5X11Extras-devel >= 5.2.0
BuildRequires:	cmake >= 2.8.12
BuildRequires:	libgcrypt-devel >= 1.6
BuildRequires:	qt5-build >= 5.2.0
BuildRequires:	qt5-linguist >= 5.2.0
BuildRequires:	qt5-qmake >= 5.2.0
BuildRequires:	rpmbuild(find_lang) >= 1.37
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
%setup -q
%patch -P0 -p1

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

%find_lang %{name} --with-qm

%{__sed} -i -e '
	s/%lang(en_plurals)/%%lang(en)/
	s/%lang(nl_NL)/%%lang(nl)/
' %{name}.lang

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

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/keepassx
%{_datadir}/mime/packages/keepassx.xml
%{_desktopdir}/keepassx.desktop
%dir %{_datadir}/keepassx
%{_datadir}/keepassx/icons
%dir %{_datadir}/keepassx/translations
%dir %{_libdir}/keepassx
%attr(755,root,root) %{_libdir}/keepassx/libkeepassx-autotype-xcb.so
%{_iconsdir}/hicolor/*x*/apps/keepassx.png
%{_iconsdir}/hicolor/*x*/mimetypes/application-x-keepassx.png
%{_iconsdir}/hicolor/scalable/apps/keepassx.svgz
