Name:           haruna
Version:        0.6.0
Release:        1
Summary:        Video player built with Qt/QML on top of libmpv
License:        CC-BY-4.0, BSD-3 Clause, GPL-3.0-or-later and WTFPL
URL:            https://github.com/g-fb/haruna
Source0:        https://github.com/g-fb/haruna/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake >= 3.15
BuildRequires:  cmake(ECM)
BuildRequires:  hicolor-icon-theme
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5FileMetaData)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Kirigami2)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5QuickControls2)
BuildRequires:  pkgconfig(mpv)

Requires: mpv

%description
Haruna is a video player built with Qt/QML on top of libmpv.

%prep
%autosetup -p1

%build
%cmake
%make_build

%install
%make_install -C build

%files
%license LICENSES/CC-BY-4.0.txt LICENSES/GPL-3.0-or-later.txt LICENSES/WTFPL.txt
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/com.georgefb.haruna.desktop
%{_datadir}/icons/hicolor/*/apps/com.georgefb.haruna.svg
%{_datadir}/metainfo/com.georgefb.haruna.appdata.xml
