%global optflags %{optflags} -O3

Name:           haruna
Version:        0.12.3
Release:        1
Summary:        Video player built with Qt/QML on top of libmpv
License:        CC-BY-4.0, BSD-3 Clause, GPL-3.0-or-later and WTFPL
URL:            https://invent.kde.org/multimedia/haruna
Source0:        https://invent.kde.org/multimedia/haruna/-/archive/v%{version}/%{name}-v%{version}.tar.bz2

BuildRequires: cmake
BuildRequires: cmake(ECM)
BuildRequires: cmake(Breeze) < 5.27.80
BuildRequires: hicolor-icon-theme
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5FileMetaData)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5IconThemes)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5Kirigami2)
BuildRequires: cmake(KF5XmlGui)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5DBus)
BuildRequires: cmake(Qt5Qml)
BuildRequires: cmake(Qt5Quick)
BuildRequires: cmake(Qt5QuickControls2)
BuildRequires: pkgconfig(mpv)
BuildRequires: pkgconfig(libavcodec)
BuildRequires: youtube-dl

Requires: mpv
Requires: kio-extras
Requires: breeze
Requires: breeze-icons
Requires: qqc2-breeze-style
Requires: youtube-dl

%description
Haruna is a video player built with Qt/QML on top of libmpv.

%prep
%autosetup -n %{name}-v%{version} -p1

%build
%cmake \
        -DCMAKE_BUILD_TYPE=Release
%make_build

%install
%make_install -C build

%find_lang %{name}

%files -f %{name}.lang
%license LICENSES/CC-BY-4.0.txt LICENSES/GPL-3.0-or-later.txt
%doc README.md
%doc %{_datadir}/doc/HTML/en/haruna/
%{_bindir}/%{name}
%{_datadir}/applications/org.kde.haruna.desktop
%{_datadir}/icons/hicolor/*/apps/haruna.svg
%{_iconsdir}/hicolor/*x*/apps/haruna.png
%{_datadir}/metainfo/org.kde.haruna.metainfo.xml
