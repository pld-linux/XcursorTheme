Summary:	X cursor packs from kde-look
Summary(pl):	Motywy kursorów X z kde-look
Name:		XcursorTheme
Version:	1.0
Release:	5
License:	Different per subpackage
Group:		X11
# The icon files have been repackaged by me in order to avoid having too much work with %prep
Source0:	%{name}.tar.bz2
# Source0-md5:	4770381266eec192263ce9c22a6d424d
Source1:	%{name}-cursorconfig
Source2:	%{name}-cursorconfig.pl.po
URL:		http://www.kde-look.org/
BuildRequires:	XFree86
BuildRequires:	gettext-devel
Requires:	XFree86
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_icondir	/usr/share/icons

%description
X cursor packs taken from kde-look. The authors are as follows:
YCursors	Daniele Pighin
vox		Mike Bryant
Red Dot		uga
GKD		noonespecial

%description -l pl
Motywy kursorów wziête z kde-look. Ich autorzy to:
YCursors	Daniele Pighin
vox		Mike Bryant
Red Dot		uga
GKD		noonespecial

%package YCursors
Summary:	YCursors cursor pack
Summary(pl):	Motyw kursorów YCursors
Group:		X11
License:	distributable (see COPYING)

%description YCursors
YCursors cursor pack by Daniele Pighin.

%description YCursors -l pl
Motyw kursorów YCursors autorstwa Daniele Pighin.

%package Red_Dot
Summary:	Red Dot cursor pack
Summary(pl):	Motyw kursorów Red Dot
Group:		X11
License:	Freeware

%description Red_Dot
Red Dot cursor pack.

%description Red_Dot -l pl
Motyw kursorów Red Dot.

%package vox
Summary:	vox cursor pack
Summary(pl):	Motyw kursorów vox
Group:		X11
License:	distributable (see COPYING)

%description vox
vox cursor pack by Mike Bryant.

%description vox -l pl
Motyw kursorów vox autorstwa Mike'a Bryanta.

%package GKD
Summary:	GKD cursor pack
Summary(pl):	Motyw kursorów GKD
Group:		X11
License:	distributable

%description GKD
GKD cursor pack.

%description GKD -l pl
Motyw kursorów GKD.

%package tux
Summary:	Tux cursor pack
Summary(pl):	Motyw kursorów Tux
Group:		X11
License:	distributable

%description tux
Tux cursor pack.

%description tux -l pl
Motyw kursorów Tux.

%package tuxshadow
Summary:	Tuxshadow cursor pack
Summary(pl):	Motyw kursorów Tuxshadow
Group:		X11
License:	distributable

%description tuxshadow
Tuxshadow cursor pack.

%description tuxshadow -l pl
Motyw kursorów Tuxshadow.

%package Golden
Summary:	Golden XCursors 3D cursor pack
Summary(pl):	Motyw kursorów Golden XCursors 3D
Group:		X11
License:	LGPL

%description Golden
Golden XCursors 3D cursor pack.

%description Golden -l pl
Motyw kursorów Golden XCursors 3D.

%package Silver
Summary:	Silver XCursors 3D cursor pack
Summary(pl):	Motyw kursorów Silver XCursors 3D
Group:		X11
License:	LGPL

%description Silver
Silver XCursors 3D cursor pack.

%description Silver -l pl
Motyw kursorów Silver XCursors 3D.

%package setup
Summary:	XCursor theme configuration script
Summary(pl):	Konfigurator motywów XCursor
Group:		X11
License:	GPL
Requires:	dialog
Requires:	fileutils
Requires:	gettext
Requires:	grep
Requires:	sed

%description setup
XCursor theme configuration script.

%description setup -l pl
Konfigurator motywów XCursor.

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
