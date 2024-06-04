%global optflags %{optflags} -O3
#define gitdate 20240226
#define gitbranch master
%define gitbranchd %(echo %{gitbranch} |sed -e 's,/,-,g')

Name:           haruna
Version:        1.1.2
Release:        %{?gitdate:0.%{gitdate}.}1
Summary:        Video player built with Qt/QML on top of libmpv
License:        CC-BY-4.0, BSD-3 Clause, GPL-3.0-or-later and WTFPL
URL:            https://invent.kde.org/multimedia/haruna
Source0:        https://invent.kde.org/multimedia/haruna/-/archive/%{?gitdate:%{gitbranch}}%{!?gitdate:v%{version}}/%{name}-%{?gitdate:%{gitbranchd}}%{!?gitdate:v%{version}}.tar.bz2

BuildRequires: cmake
BuildRequires: cmake(ECM)
BuildRequires: cmake(Breeze) >= 6.0.0
BuildRequires: hicolor-icon-theme
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Core5Compat)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6QuickControls2)
BuildRequires: cmake(MpvQt)
BuildRequires: cmake(KF6ColorScheme)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6FileMetaData)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6Kirigami)
BuildRequires: cmake(KF6WindowSystem)
BuildRequires: pkgconfig(mpv)
BuildRequires: pkgconfig(libavcodec)
BuildRequires: yt-dlp

Requires: mpv
Requires: (kf6-breeze-icons or breeze-icons)
Requires: plasma6-qqc2-breeze-style
Requires: (yt-dlp or youtube-dl)
Recommends: plasma6-kio-extras

%description
Haruna is a video player built with Qt/QML on top of libmpv.

%prep
%autosetup -n %{name}-%{?gitdate:%{gitbranchd}}%{!?gitdate:v%{version}} -p1
%cmake \
	-DQT_MAJOR_VERSION=6 \
        -DCMAKE_BUILD_TYPE=Release \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

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
