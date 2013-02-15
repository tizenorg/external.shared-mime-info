Name:       shared-mime-info
Summary:    FreeDesktop.org shared MIME database and spec
Version:    0.60
Release:    4
Group:      misc
License:    GPLv2
Source0:    shared-mime-info-0.60.tar.gz
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  intltool >= 0.35
BuildRequires:  libxml2

%description
FreeDesktop.org shared MIME database and spec
 This is the shared MIME-info database from the X Desktop Group. It is required
 by any program complying to the Shared MIME-Info Database spec, which is also
 included in this package.
 .
 At this time ROX and GNOME use this database. KDE is expected to follow soon, 
 and hopefully others too..

%prep
%setup -q -n %{name}-%{version}

%build
%configure --disable-static
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install




%files
%defattr(-,root,root,-)
/usr/bin/update-mime-database
/usr/share/*
%manifest shared-mime-info.manifest
