%global optflags %{optflags} -O3

Name:           haruna
Version:        0.6.3.1
Release:        1
Summary:        Video player built with Qt/QML on top of libmpv
License:        CC-BY-4.0, BSD-3 Clause, GPL-3.0-or-later and WTFPL
URL:            https://github.com/g-fb/haruna
Source0:        https://invent.kde.org/multimedia/haruna/-/archive/%{version}/%{name}-%{version}.tar.bz2

BuildRequires: cmake
BuildRequires: cmake(ECM)
BuildRequires: cmake(Breeze)
BuildRequires: hicolor-icon-theme
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

Requires: mpv
Requires: kio-extras
Requires: breeze
Requires: breeze-icons
Requires: qqc2-breeze-style
Requires: youtube-dl

%description
Haruna is a video player built with Qt/QML on top of libmpv.

%prep
%autosetup -p1

%build
%cmake \
        -DCMAKE_BUILD_TYPE=Release
%make_build

%install
%make_install -C build

%files
%license LICENSES/CC-BY-4.0.txt LICENSES/GPL-3.0-or-later.txt LICENSES/WTFPL.txt
%doc README.md
%{_bindir}/%{name}
#{_datadir}/applications/org.kde.haruna.desktop
#{_datadir}/icons/hicolor/*/apps/org.kde.haruna.svg
#{_datadir}/metainfo/org.kde.haruna.appdata.xml
