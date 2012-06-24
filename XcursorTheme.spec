#
# TODO: cursorconfig doesn't work on TH dialog
#	(removing unsupported --one-column option doesn't help)
#
Summary:	X cursor packs from kde-look
Summary(pl):	Motywy kursor�w X z kde-look
Name:		XcursorTheme
Version:	1.0
Release:	9
License:	Different per subpackage
Group:		Themes
# The icon files have been repackaged by me in order to avoid having too much work with %%prep
Source0:	XFree86-Xcursor-packs.tar.bz2
# Source0-md5:	4770381266eec192263ce9c22a6d424d
Source1:	%{name}-cursorconfig
Source2:	%{name}-cursorconfig.pl.po
URL:		http://www.kde-look.org/
BuildRequires:	gettext-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_icondir	/usr/share/icons

%description
X cursor packs taken from kde-look. The authors are as follows:
YCursors	Daniele Pighin
vox		Mike Bryant
Red Dot		uga
GKD		noonespecial

%description -l pl
Motywy kursor�w wzi�te z kde-look. Ich autorzy to:
YCursors	Daniele Pighin
vox		Mike Bryant
Red Dot		uga
GKD		noonespecial

%package YCursors
Summary:	YCursors cursor pack
Summary(pl):	Motyw kursor�w YCursors
License:	distributable (see COPYING)
Group:		Themes
Obsoletes:	XFree86-Xcursor-packs-YCursors

%description YCursors
YCursors cursor pack by Daniele Pighin.

%description YCursors -l pl
Motyw kursor�w YCursors autorstwa Daniele Pighin.

%package Red_Dot
Summary:	Red Dot cursor pack
Summary(pl):	Motyw kursor�w Red Dot
License:	Freeware
Group:		Themes
Obsoletes:	XFree86-Xcursor-packs-Red_Dot

%description Red_Dot
Red Dot cursor pack.

%description Red_Dot -l pl
Motyw kursor�w Red Dot.

%package vox
Summary:	vox cursor pack
Summary(pl):	Motyw kursor�w vox
License:	distributable (see COPYING)
Group:		Themes
Obsoletes:	XFree86-Xcursor-packs-vox

%description vox
vox cursor pack by Mike Bryant.

%description vox -l pl
Motyw kursor�w vox autorstwa Mike'a Bryanta.

%package GKD
Summary:	GKD cursor pack
Summary(pl):	Motyw kursor�w GKD
License:	distributable
Group:		Themes
Obsoletes:	XFree86-Xcursor-packs-GKD

%description GKD
GKD cursor pack.

%description GKD -l pl
Motyw kursor�w GKD.

%package tux
Summary:	Tux cursor pack
Summary(pl):	Motyw kursor�w Tux
License:	distributable
Group:		Themes
Obsoletes:	XFree86-Xcursor-packs-tux

%description tux
Tux cursor pack.

%description tux -l pl
Motyw kursor�w Tux.

%package tuxshadow
Summary:	Tuxshadow cursor pack
Summary(pl):	Motyw kursor�w Tuxshadow
License:	distributable
Group:		Themes
Obsoletes:	XFree86-Xcursor-packs-tuxshadow

%description tuxshadow
Tuxshadow cursor pack.

%description tuxshadow -l pl
Motyw kursor�w Tuxshadow.

%package Golden
Summary:	Golden XCursors 3D cursor pack
Summary(pl):	Motyw kursor�w Golden XCursors 3D
License:	LGPL
Group:		Themes
Obsoletes:	XFree86-Xcursor-packs-Golden

%description Golden
Golden XCursors 3D cursor pack.

%description Golden -l pl
Motyw kursor�w Golden XCursors 3D.

%package Silver
Summary:	Silver XCursors 3D cursor pack
Summary(pl):	Motyw kursor�w Silver XCursors 3D
License:	LGPL
Group:		Themes
Obsoletes:	XFree86-Xcursor-packs-Silver

%description Silver
Silver XCursors 3D cursor pack.

%description Silver -l pl
Motyw kursor�w Silver XCursors 3D.

%package setup
Summary:	XCursor theme configuration script
Summary(pl):	Konfigurator motyw�w XCursor
Group:		Themes
License:	GPL
Requires:	dialog
Requires:	fileutils
Requires:	gettext
Requires:	grep
Requires:	sed
Obsoletes:	XFree86-Xcursor-packs-setup

%description setup
XCursor theme configuration script.

%description setup -l pl
Konfigurator motyw�w XCursor.

%prep
%setup -q -n cursors

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/locale/pl/LC_MESSAGES} \
	$RPM_BUILD_ROOT%{_icondir}/{GKD,YCursors,reddot,vox,tux,tuxshadow,gold,Silver}/cursors

# preserve symlinks
cp -df GKD/*		$RPM_BUILD_ROOT%{_icondir}/GKD/cursors
cp -df YCursors/*	$RPM_BUILD_ROOT%{_icondir}/YCursors/cursors
cp -df reddot/*		$RPM_BUILD_ROOT%{_icondir}/reddot/cursors
cp -df vox/*		$RPM_BUILD_ROOT%{_icondir}/vox/cursors
cp -df tuxcursor/*	$RPM_BUILD_ROOT%{_icondir}/tux/cursors
cp -df tuxshadow/*	$RPM_BUILD_ROOT%{_icondir}/tuxshadow/cursors
cp -df gold/*		$RPM_BUILD_ROOT%{_icondir}/gold/cursors
cp -df Silver/*		$RPM_BUILD_ROOT%{_icondir}/Silver/cursors
install %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/cursorconfig
msgfmt -v %{SOURCE2} -o $RPM_BUILD_ROOT%{_datadir}/locale/pl/LC_MESSAGES/cursorconfig.mo

%find_lang cursorconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files YCursors
%defattr(644,root,root,755)
%doc doc/YCursors/*
%{_icondir}/YCursors

%files vox
%defattr(644,root,root,755)
%doc doc/vox/*
%{_icondir}/vox

%files Red_Dot
%defattr(644,root,root,755)
%{_icondir}/reddot

%files GKD
%defattr(644,root,root,755)
%{_icondir}/GKD

%files tux
%defattr(644,root,root,755)
%{_icondir}/tux

%files tuxshadow
%defattr(644,root,root,755)
%{_icondir}/tuxshadow

%files Golden
%defattr(644,root,root,755)
%doc doc/gold/*
%{_icondir}/gold

%files Silver
%defattr(644,root,root,755)
%doc doc/Silver/*
%{_icondir}/Silver


%files setup -f cursorconfig.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cursorconfig
