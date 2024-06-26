%define debug_package %{nil}
%define __os_install_post %{nil}

Name: MacVentura-kde
Summary: MacVentura KDE Theme

Version: {{{ git_dir_version }}}
License: GPLv3
Release: 1%{?dist}
URL:     https://github.com/vinceliuice/MacVentura-kde
Source0: %{url}/archive/master/MacVentura-kde-main.tar.gz

BuildArch: noarch
BuildRequires: coreutils

#Requires: kvantum

%description
MacVentura KDE theme

%prep
%setup -q -n %{name}-main

%install
AURORAE_DIR=%{buildroot}%{_datadir}/aurorae/themes
SCHEMES_DIR=%{buildroot}%{_datadir}/color-schemes
PLASMA_DIR=%{buildroot}%{_datadir}/plasma/desktoptheme
LOOKFEEL_DIR=%{buildroot}%{_datadir}/plasma/look-and-feel
LAYOUT_TEMPLATE_DIR=%{buildroot}%{_datadir}/plasma/layout-templates
PLASMOID_DIR=%{buildroot}%{_datadir}/plasma/plasmoids
KVANTUM_DIR=%{buildroot}%{_datadir}/Kvantum
WALLPAPER_DIR=%{buildroot}%{_datadir}/wallpapers
LATTE_DIR=%{buildroot}%{_datadir}/latte/config
SDDM_DIR=%{buildroot}%{_datadir}/sddm/themes

mkdir -p ${AURORAE_DIR}
mkdir -p ${SCHEMES_DIR}
mkdir -p ${PLASMA_DIR}
mkdir -p ${LOOKFEEL_DIR}
mkdir -p ${LAYOUT_TEMPLATE_DIR}
mkdir -p ${PLASMOID_DIR}
mkdir -p ${KVANTUM_DIR}
mkdir -p ${WALLPAPER_DIR}
mkdir -p ${LATTE_DIR}
mkdir -p ${SDDM_DIR}

cp -r aurorae/Sharp/MacVentura-Dark/ ${AURORAE_DIR}/MacVentura-Dark
cp -r aurorae/Sharp/MacVentura-Light/ ${AURORAE_DIR}/MacVentura-Light
cp -r Kvantum/*                       ${KVANTUM_DIR}
cp -r color-schemes/*                 ${SCHEMES_DIR}
cp -r plasma/desktoptheme/MacVentura*   ${PLASMA_DIR}
cp -r plasma/desktoptheme/icons       ${PLASMA_DIR}/MacVentura-Light
cp -r plasma/desktoptheme/icons       ${PLASMA_DIR}/MacVentura-Dark
cp -r plasma/look-and-feel/*          ${LOOKFEEL_DIR}
cp -r plasma/layout-templates/*       ${LAYOUT_TEMPLATE_DIR}
cp -r plasma/plasmoids/*              ${PLASMOID_DIR}
cp -r wallpaper/MacVentura            ${WALLPAPER_DIR}
cp -r wallpaper/MacVentura-Dark       ${WALLPAPER_DIR}
cp -r wallpaper/MacVentura-Light      ${WALLPAPER_DIR}
cp -r latte-dock/*                    ${LATTE_DIR}

%files
%{_datadir}/aurorae/themes
%{_datadir}/color-schemes
%{_datadir}/plasma/desktoptheme
%{_datadir}/plasma/look-and-feel
%{_datadir}/plasma/layout-templates
%{_datadir}/plasma/plasmoids
%{_datadir}/Kvantum
%{_datadir}/wallpapers
%{_datadir}/latte/config

%changelog
{{{ git_dir_changelog }}}
