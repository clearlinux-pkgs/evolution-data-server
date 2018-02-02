#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : evolution-data-server
Version  : 3.26.4
Release  : 23
URL      : https://download.gnome.org/sources/evolution-data-server/3.26/evolution-data-server-3.26.4.tar.xz
Source0  : https://download.gnome.org/sources/evolution-data-server/3.26/evolution-data-server-3.26.4.tar.xz
Summary  : The evolution data server for the calendar and addressbook
Group    : Development/Tools
License  : LGPL-2.0
Requires: evolution-data-server-config
Requires: evolution-data-server-lib
Requires: evolution-data-server-bin
Requires: evolution-data-server-data
Requires: evolution-data-server-locales
BuildRequires : cmake
BuildRequires : db-dev
BuildRequires : e2fsprogs-dev
BuildRequires : gobject-introspection-dev
BuildRequires : gperf
BuildRequires : intltool
BuildRequires : libsecret-dev
BuildRequires : libxml2-dev
BuildRequires : nss-dev
BuildRequires : openldap-dev
BuildRequires : pkgconfig(krb5)
BuildRequires : pkgconfig(libgdata)
BuildRequires : pkgconfig(libical)
BuildRequires : pkgconfig(libsoup-2.4)
BuildRequires : python3
BuildRequires : sqlite-autoconf-dev
Patch1: 0001-do-python3.patch

%description
The Evolution Data Server package provides a unified backend for programs that work with
contacts, tasks, and calendar information. It was originally developed for Evolution
(hence the name), but is now used by other packages as well.

%package bin
Summary: bin components for the evolution-data-server package.
Group: Binaries
Requires: evolution-data-server-data
Requires: evolution-data-server-config

%description bin
bin components for the evolution-data-server package.


%package config
Summary: config components for the evolution-data-server package.
Group: Default

%description config
config components for the evolution-data-server package.


%package data
Summary: data components for the evolution-data-server package.
Group: Data

%description data
data components for the evolution-data-server package.


%package dev
Summary: dev components for the evolution-data-server package.
Group: Development
Requires: evolution-data-server-lib
Requires: evolution-data-server-bin
Requires: evolution-data-server-data
Provides: evolution-data-server-devel

%description dev
dev components for the evolution-data-server package.


%package lib
Summary: lib components for the evolution-data-server package.
Group: Libraries
Requires: evolution-data-server-data

%description lib
lib components for the evolution-data-server package.


%package locales
Summary: locales components for the evolution-data-server package.
Group: Default

%description locales
locales components for the evolution-data-server package.


%prep
%setup -q -n evolution-data-server-3.26.4
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1515419270
mkdir clr-build
pushd clr-build
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
cmake .. -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX=/usr -DBUILD_SHARED_LIBS:BOOL=ON -DLIB_INSTALL_DIR:PATH=/usr/lib64 -DCMAKE_AR=/usr/bin/gcc-ar -DLIB_SUFFIX=64 -DCMAKE_BUILD_TYPE=RelWithDebInfo -DCMAKE_RANLIB=/usr/bin/gcc-ranlib -DENABLE_GOOGLE_AUTH=OFF  -DENABLE_UOA=OFF  -DENABLE_WEATHER=OFF
make VERBOSE=1  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1515419270
rm -rf %{buildroot}
pushd clr-build
%make_install
popd
%find_lang evolution-data-server

%files
%defattr(-,root,root,-)
/usr/lib64/evolution-data-server/camel-providers/libcamelimapx.urls
/usr/lib64/evolution-data-server/camel-providers/libcamellocal.urls
/usr/lib64/evolution-data-server/camel-providers/libcamelnntp.urls
/usr/lib64/evolution-data-server/camel-providers/libcamelpop3.urls
/usr/lib64/evolution-data-server/camel-providers/libcamelsendmail.urls
/usr/lib64/evolution-data-server/camel-providers/libcamelsmtp.urls

%files bin
%defattr(-,root,root,-)
/usr/libexec/camel-gpg-photo-saver
/usr/libexec/camel-index-control-1.2
/usr/libexec/camel-lock-helper-1.2
/usr/libexec/evolution-addressbook-factory
/usr/libexec/evolution-addressbook-factory-subprocess
/usr/libexec/evolution-calendar-factory
/usr/libexec/evolution-calendar-factory-subprocess
/usr/libexec/evolution-data-server/addressbook-export
/usr/libexec/evolution-data-server/csv2vcard
/usr/libexec/evolution-data-server/list-sources
/usr/libexec/evolution-scan-gconf-tree-xml
/usr/libexec/evolution-source-registry
/usr/libexec/evolution-user-prompter

%files config
%defattr(-,root,root,-)
/usr/lib/systemd/user/evolution-addressbook-factory.service
/usr/lib/systemd/user/evolution-calendar-factory.service
/usr/lib/systemd/user/evolution-source-registry.service
/usr/lib/systemd/user/evolution-user-prompter.service

%files data
%defattr(-,root,root,-)
/usr/share/GConf/gsettings/evolution-data-server.convert
/usr/share/dbus-1/services/org.gnome.evolution.dataserver.AddressBook.service
/usr/share/dbus-1/services/org.gnome.evolution.dataserver.Calendar.service
/usr/share/dbus-1/services/org.gnome.evolution.dataserver.Sources.service
/usr/share/dbus-1/services/org.gnome.evolution.dataserver.UserPrompter.service
/usr/share/evolution-data-server/evolutionperson.schema
/usr/share/glib-2.0/schemas/org.gnome.Evolution.DefaultSources.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.evolution-data-server.addressbook.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.evolution-data-server.calendar.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.evolution-data-server.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.evolution.eds-shell.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.evolution.shell.network-config.gschema.xml
/usr/share/pixmaps/evolution-data-server/category_birthday_16.png
/usr/share/pixmaps/evolution-data-server/category_business_16.png
/usr/share/pixmaps/evolution-data-server/category_favorites_16.png
/usr/share/pixmaps/evolution-data-server/category_gifts_16.png
/usr/share/pixmaps/evolution-data-server/category_goals_16.png
/usr/share/pixmaps/evolution-data-server/category_holiday-cards_16.png
/usr/share/pixmaps/evolution-data-server/category_holiday_16.png
/usr/share/pixmaps/evolution-data-server/category_hot-contacts_16.png
/usr/share/pixmaps/evolution-data-server/category_ideas_16.png
/usr/share/pixmaps/evolution-data-server/category_international_16.png
/usr/share/pixmaps/evolution-data-server/category_key-customer_16.png
/usr/share/pixmaps/evolution-data-server/category_miscellaneous_16.png
/usr/share/pixmaps/evolution-data-server/category_personal_16.png
/usr/share/pixmaps/evolution-data-server/category_phonecalls_16.png
/usr/share/pixmaps/evolution-data-server/category_status_16.png
/usr/share/pixmaps/evolution-data-server/category_strategies_16.png
/usr/share/pixmaps/evolution-data-server/category_suppliers_16.png
/usr/share/pixmaps/evolution-data-server/category_time-and-expenses_16.png

%files dev
%defattr(-,root,root,-)
/usr/include/evolution-data-server/camel/camel-address.h
/usr/include/evolution-data-server/camel/camel-async-closure.h
/usr/include/evolution-data-server/camel/camel-block-file.h
/usr/include/evolution-data-server/camel/camel-certdb.h
/usr/include/evolution-data-server/camel/camel-charset-map.h
/usr/include/evolution-data-server/camel/camel-cipher-context.h
/usr/include/evolution-data-server/camel/camel-data-cache.h
/usr/include/evolution-data-server/camel/camel-data-wrapper.h
/usr/include/evolution-data-server/camel/camel-db.h
/usr/include/evolution-data-server/camel/camel-debug.h
/usr/include/evolution-data-server/camel/camel-enums.h
/usr/include/evolution-data-server/camel/camel-enumtypes.h
/usr/include/evolution-data-server/camel/camel-file-utils.h
/usr/include/evolution-data-server/camel/camel-filter-driver.h
/usr/include/evolution-data-server/camel/camel-filter-input-stream.h
/usr/include/evolution-data-server/camel/camel-filter-output-stream.h
/usr/include/evolution-data-server/camel/camel-filter-search.h
/usr/include/evolution-data-server/camel/camel-folder-search.h
/usr/include/evolution-data-server/camel/camel-folder-summary.h
/usr/include/evolution-data-server/camel/camel-folder-thread.h
/usr/include/evolution-data-server/camel/camel-folder.h
/usr/include/evolution-data-server/camel/camel-gpg-context.h
/usr/include/evolution-data-server/camel/camel-html-parser.h
/usr/include/evolution-data-server/camel/camel-iconv.h
/usr/include/evolution-data-server/camel/camel-index.h
/usr/include/evolution-data-server/camel/camel-internet-address.h
/usr/include/evolution-data-server/camel/camel-junk-filter.h
/usr/include/evolution-data-server/camel/camel-local-settings.h
/usr/include/evolution-data-server/camel/camel-lock-client.h
/usr/include/evolution-data-server/camel/camel-lock-helper.h
/usr/include/evolution-data-server/camel/camel-lock.h
/usr/include/evolution-data-server/camel/camel-medium.h
/usr/include/evolution-data-server/camel/camel-memchunk.h
/usr/include/evolution-data-server/camel/camel-mempool.h
/usr/include/evolution-data-server/camel/camel-message-info-base.h
/usr/include/evolution-data-server/camel/camel-message-info.h
/usr/include/evolution-data-server/camel/camel-mime-filter-basic.h
/usr/include/evolution-data-server/camel/camel-mime-filter-bestenc.h
/usr/include/evolution-data-server/camel/camel-mime-filter-canon.h
/usr/include/evolution-data-server/camel/camel-mime-filter-charset.h
/usr/include/evolution-data-server/camel/camel-mime-filter-crlf.h
/usr/include/evolution-data-server/camel/camel-mime-filter-enriched.h
/usr/include/evolution-data-server/camel/camel-mime-filter-from.h
/usr/include/evolution-data-server/camel/camel-mime-filter-gzip.h
/usr/include/evolution-data-server/camel/camel-mime-filter-html.h
/usr/include/evolution-data-server/camel/camel-mime-filter-index.h
/usr/include/evolution-data-server/camel/camel-mime-filter-linewrap.h
/usr/include/evolution-data-server/camel/camel-mime-filter-pgp.h
/usr/include/evolution-data-server/camel/camel-mime-filter-progress.h
/usr/include/evolution-data-server/camel/camel-mime-filter-tohtml.h
/usr/include/evolution-data-server/camel/camel-mime-filter-windows.h
/usr/include/evolution-data-server/camel/camel-mime-filter-yenc.h
/usr/include/evolution-data-server/camel/camel-mime-filter.h
/usr/include/evolution-data-server/camel/camel-mime-message.h
/usr/include/evolution-data-server/camel/camel-mime-parser.h
/usr/include/evolution-data-server/camel/camel-mime-part-utils.h
/usr/include/evolution-data-server/camel/camel-mime-part.h
/usr/include/evolution-data-server/camel/camel-mime-utils.h
/usr/include/evolution-data-server/camel/camel-movemail.h
/usr/include/evolution-data-server/camel/camel-msgport.h
/usr/include/evolution-data-server/camel/camel-multipart-encrypted.h
/usr/include/evolution-data-server/camel/camel-multipart-signed.h
/usr/include/evolution-data-server/camel/camel-multipart.h
/usr/include/evolution-data-server/camel/camel-name-value-array.h
/usr/include/evolution-data-server/camel/camel-named-flags.h
/usr/include/evolution-data-server/camel/camel-net-utils.h
/usr/include/evolution-data-server/camel/camel-network-service.h
/usr/include/evolution-data-server/camel/camel-network-settings.h
/usr/include/evolution-data-server/camel/camel-nntp-address.h
/usr/include/evolution-data-server/camel/camel-null-output-stream.h
/usr/include/evolution-data-server/camel/camel-object-bag.h
/usr/include/evolution-data-server/camel/camel-object.h
/usr/include/evolution-data-server/camel/camel-offline-folder.h
/usr/include/evolution-data-server/camel/camel-offline-settings.h
/usr/include/evolution-data-server/camel/camel-offline-store.h
/usr/include/evolution-data-server/camel/camel-operation.h
/usr/include/evolution-data-server/camel/camel-partition-table.h
/usr/include/evolution-data-server/camel/camel-provider.h
/usr/include/evolution-data-server/camel/camel-sasl-anonymous.h
/usr/include/evolution-data-server/camel/camel-sasl-cram-md5.h
/usr/include/evolution-data-server/camel/camel-sasl-digest-md5.h
/usr/include/evolution-data-server/camel/camel-sasl-gssapi.h
/usr/include/evolution-data-server/camel/camel-sasl-login.h
/usr/include/evolution-data-server/camel/camel-sasl-ntlm.h
/usr/include/evolution-data-server/camel/camel-sasl-plain.h
/usr/include/evolution-data-server/camel/camel-sasl-popb4smtp.h
/usr/include/evolution-data-server/camel/camel-sasl.h
/usr/include/evolution-data-server/camel/camel-search-private.h
/usr/include/evolution-data-server/camel/camel-search-sql-sexp.h
/usr/include/evolution-data-server/camel/camel-service.h
/usr/include/evolution-data-server/camel/camel-session.h
/usr/include/evolution-data-server/camel/camel-settings.h
/usr/include/evolution-data-server/camel/camel-sexp.h
/usr/include/evolution-data-server/camel/camel-smime-context.h
/usr/include/evolution-data-server/camel/camel-store-settings.h
/usr/include/evolution-data-server/camel/camel-store-summary.h
/usr/include/evolution-data-server/camel/camel-store.h
/usr/include/evolution-data-server/camel/camel-stream-buffer.h
/usr/include/evolution-data-server/camel/camel-stream-filter.h
/usr/include/evolution-data-server/camel/camel-stream-fs.h
/usr/include/evolution-data-server/camel/camel-stream-mem.h
/usr/include/evolution-data-server/camel/camel-stream-null.h
/usr/include/evolution-data-server/camel/camel-stream-process.h
/usr/include/evolution-data-server/camel/camel-stream.h
/usr/include/evolution-data-server/camel/camel-string-utils.h
/usr/include/evolution-data-server/camel/camel-subscribable.h
/usr/include/evolution-data-server/camel/camel-text-index.h
/usr/include/evolution-data-server/camel/camel-transport.h
/usr/include/evolution-data-server/camel/camel-trie.h
/usr/include/evolution-data-server/camel/camel-uid-cache.h
/usr/include/evolution-data-server/camel/camel-url-scanner.h
/usr/include/evolution-data-server/camel/camel-url.h
/usr/include/evolution-data-server/camel/camel-utf8.h
/usr/include/evolution-data-server/camel/camel-utils.h
/usr/include/evolution-data-server/camel/camel-vee-data-cache.h
/usr/include/evolution-data-server/camel/camel-vee-folder.h
/usr/include/evolution-data-server/camel/camel-vee-message-info.h
/usr/include/evolution-data-server/camel/camel-vee-store.h
/usr/include/evolution-data-server/camel/camel-vee-summary.h
/usr/include/evolution-data-server/camel/camel-vtrash-folder.h
/usr/include/evolution-data-server/camel/camel-weak-ref-group.h
/usr/include/evolution-data-server/camel/camel.h
/usr/include/evolution-data-server/libebackend/e-backend-enums.h
/usr/include/evolution-data-server/libebackend/e-backend-enumtypes.h
/usr/include/evolution-data-server/libebackend/e-backend-factory.h
/usr/include/evolution-data-server/libebackend/e-backend.h
/usr/include/evolution-data-server/libebackend/e-cache-reaper.h
/usr/include/evolution-data-server/libebackend/e-cache.h
/usr/include/evolution-data-server/libebackend/e-collection-backend-factory.h
/usr/include/evolution-data-server/libebackend/e-collection-backend.h
/usr/include/evolution-data-server/libebackend/e-data-factory.h
/usr/include/evolution-data-server/libebackend/e-db3-utils.h
/usr/include/evolution-data-server/libebackend/e-dbhash.h
/usr/include/evolution-data-server/libebackend/e-dbus-server.h
/usr/include/evolution-data-server/libebackend/e-file-cache.h
/usr/include/evolution-data-server/libebackend/e-oauth2-support.h
/usr/include/evolution-data-server/libebackend/e-offline-listener.h
/usr/include/evolution-data-server/libebackend/e-server-side-source-credentials-provider.h
/usr/include/evolution-data-server/libebackend/e-server-side-source.h
/usr/include/evolution-data-server/libebackend/e-source-registry-server.h
/usr/include/evolution-data-server/libebackend/e-sqlite3-vfs.h
/usr/include/evolution-data-server/libebackend/e-subprocess-factory.h
/usr/include/evolution-data-server/libebackend/e-user-prompter-server-extension.h
/usr/include/evolution-data-server/libebackend/e-user-prompter-server.h
/usr/include/evolution-data-server/libebackend/e-user-prompter.h
/usr/include/evolution-data-server/libebackend/e-webdav-collection-backend.h
/usr/include/evolution-data-server/libebackend/libebackend.h
/usr/include/evolution-data-server/libebook-contacts/e-address-western.h
/usr/include/evolution-data-server/libebook-contacts/e-book-contacts-enumtypes.h
/usr/include/evolution-data-server/libebook-contacts/e-book-contacts-types.h
/usr/include/evolution-data-server/libebook-contacts/e-book-query.h
/usr/include/evolution-data-server/libebook-contacts/e-contact.h
/usr/include/evolution-data-server/libebook-contacts/e-name-western.h
/usr/include/evolution-data-server/libebook-contacts/e-phone-number.h
/usr/include/evolution-data-server/libebook-contacts/e-source-backend-summary-setup.h
/usr/include/evolution-data-server/libebook-contacts/e-vcard.h
/usr/include/evolution-data-server/libebook-contacts/libebook-contacts.h
/usr/include/evolution-data-server/libebook/e-book-client-cursor.h
/usr/include/evolution-data-server/libebook/e-book-client-view.h
/usr/include/evolution-data-server/libebook/e-book-client.h
/usr/include/evolution-data-server/libebook/e-book-enumtypes.h
/usr/include/evolution-data-server/libebook/e-book-types.h
/usr/include/evolution-data-server/libebook/e-book-view.h
/usr/include/evolution-data-server/libebook/e-book.h
/usr/include/evolution-data-server/libebook/e-destination.h
/usr/include/evolution-data-server/libebook/libebook.h
/usr/include/evolution-data-server/libecal/e-cal-check-timezones.h
/usr/include/evolution-data-server/libecal/e-cal-client-view.h
/usr/include/evolution-data-server/libecal/e-cal-client.h
/usr/include/evolution-data-server/libecal/e-cal-component.h
/usr/include/evolution-data-server/libecal/e-cal-enumtypes.h
/usr/include/evolution-data-server/libecal/e-cal-recur.h
/usr/include/evolution-data-server/libecal/e-cal-system-timezone.h
/usr/include/evolution-data-server/libecal/e-cal-time-util.h
/usr/include/evolution-data-server/libecal/e-cal-types.h
/usr/include/evolution-data-server/libecal/e-cal-util.h
/usr/include/evolution-data-server/libecal/e-cal-view.h
/usr/include/evolution-data-server/libecal/e-cal.h
/usr/include/evolution-data-server/libecal/e-timezone-cache.h
/usr/include/evolution-data-server/libecal/libecal.h
/usr/include/evolution-data-server/libedata-book/e-book-backend-cache.h
/usr/include/evolution-data-server/libedata-book/e-book-backend-db-cache.h
/usr/include/evolution-data-server/libedata-book/e-book-backend-factory.h
/usr/include/evolution-data-server/libedata-book/e-book-backend-sexp.h
/usr/include/evolution-data-server/libedata-book/e-book-backend-sqlitedb.h
/usr/include/evolution-data-server/libedata-book/e-book-backend-summary.h
/usr/include/evolution-data-server/libedata-book/e-book-backend.h
/usr/include/evolution-data-server/libedata-book/e-book-cache.h
/usr/include/evolution-data-server/libedata-book/e-book-meta-backend.h
/usr/include/evolution-data-server/libedata-book/e-book-sqlite.h
/usr/include/evolution-data-server/libedata-book/e-data-book-cursor-cache.h
/usr/include/evolution-data-server/libedata-book/e-data-book-cursor-sqlite.h
/usr/include/evolution-data-server/libedata-book/e-data-book-cursor.h
/usr/include/evolution-data-server/libedata-book/e-data-book-direct.h
/usr/include/evolution-data-server/libedata-book/e-data-book-factory.h
/usr/include/evolution-data-server/libedata-book/e-data-book-view.h
/usr/include/evolution-data-server/libedata-book/e-data-book.h
/usr/include/evolution-data-server/libedata-book/e-subprocess-book-factory.h
/usr/include/evolution-data-server/libedata-book/libedata-book.h
/usr/include/evolution-data-server/libedata-cal/e-cal-backend-cache.h
/usr/include/evolution-data-server/libedata-cal/e-cal-backend-factory.h
/usr/include/evolution-data-server/libedata-cal/e-cal-backend-intervaltree.h
/usr/include/evolution-data-server/libedata-cal/e-cal-backend-sexp.h
/usr/include/evolution-data-server/libedata-cal/e-cal-backend-store.h
/usr/include/evolution-data-server/libedata-cal/e-cal-backend-sync.h
/usr/include/evolution-data-server/libedata-cal/e-cal-backend-util.h
/usr/include/evolution-data-server/libedata-cal/e-cal-backend.h
/usr/include/evolution-data-server/libedata-cal/e-cal-cache.h
/usr/include/evolution-data-server/libedata-cal/e-cal-meta-backend.h
/usr/include/evolution-data-server/libedata-cal/e-data-cal-factory.h
/usr/include/evolution-data-server/libedata-cal/e-data-cal-view.h
/usr/include/evolution-data-server/libedata-cal/e-data-cal.h
/usr/include/evolution-data-server/libedata-cal/e-subprocess-cal-factory.h
/usr/include/evolution-data-server/libedata-cal/libedata-cal.h
/usr/include/evolution-data-server/libedataserver/e-cancellable-locks.h
/usr/include/evolution-data-server/libedataserver/e-categories.h
/usr/include/evolution-data-server/libedataserver/e-client.h
/usr/include/evolution-data-server/libedataserver/e-collator.h
/usr/include/evolution-data-server/libedataserver/e-credentials.h
/usr/include/evolution-data-server/libedataserver/e-data-server-util.h
/usr/include/evolution-data-server/libedataserver/e-debug-log.h
/usr/include/evolution-data-server/libedataserver/e-extensible.h
/usr/include/evolution-data-server/libedataserver/e-extension.h
/usr/include/evolution-data-server/libedataserver/e-flag.h
/usr/include/evolution-data-server/libedataserver/e-free-form-exp.h
/usr/include/evolution-data-server/libedataserver/e-gdbus-templates.h
/usr/include/evolution-data-server/libedataserver/e-iterator.h
/usr/include/evolution-data-server/libedataserver/e-list-iterator.h
/usr/include/evolution-data-server/libedataserver/e-list.h
/usr/include/evolution-data-server/libedataserver/e-memory.h
/usr/include/evolution-data-server/libedataserver/e-module.h
/usr/include/evolution-data-server/libedataserver/e-network-monitor.h
/usr/include/evolution-data-server/libedataserver/e-operation-pool.h
/usr/include/evolution-data-server/libedataserver/e-proxy.h
/usr/include/evolution-data-server/libedataserver/e-secret-store.h
/usr/include/evolution-data-server/libedataserver/e-sexp.h
/usr/include/evolution-data-server/libedataserver/e-soup-auth-bearer.h
/usr/include/evolution-data-server/libedataserver/e-soup-session.h
/usr/include/evolution-data-server/libedataserver/e-soup-ssl-trust.h
/usr/include/evolution-data-server/libedataserver/e-source-address-book.h
/usr/include/evolution-data-server/libedataserver/e-source-alarms.h
/usr/include/evolution-data-server/libedataserver/e-source-authentication.h
/usr/include/evolution-data-server/libedataserver/e-source-autocomplete.h
/usr/include/evolution-data-server/libedataserver/e-source-autoconfig.h
/usr/include/evolution-data-server/libedataserver/e-source-backend.h
/usr/include/evolution-data-server/libedataserver/e-source-calendar.h
/usr/include/evolution-data-server/libedataserver/e-source-camel.h
/usr/include/evolution-data-server/libedataserver/e-source-collection.h
/usr/include/evolution-data-server/libedataserver/e-source-contacts.h
/usr/include/evolution-data-server/libedataserver/e-source-credentials-provider-impl-google.h
/usr/include/evolution-data-server/libedataserver/e-source-credentials-provider-impl-password.h
/usr/include/evolution-data-server/libedataserver/e-source-credentials-provider-impl.h
/usr/include/evolution-data-server/libedataserver/e-source-credentials-provider.h
/usr/include/evolution-data-server/libedataserver/e-source-enums.h
/usr/include/evolution-data-server/libedataserver/e-source-enumtypes.h
/usr/include/evolution-data-server/libedataserver/e-source-extension.h
/usr/include/evolution-data-server/libedataserver/e-source-goa.h
/usr/include/evolution-data-server/libedataserver/e-source-ldap.h
/usr/include/evolution-data-server/libedataserver/e-source-local.h
/usr/include/evolution-data-server/libedataserver/e-source-mail-account.h
/usr/include/evolution-data-server/libedataserver/e-source-mail-composition.h
/usr/include/evolution-data-server/libedataserver/e-source-mail-identity.h
/usr/include/evolution-data-server/libedataserver/e-source-mail-signature.h
/usr/include/evolution-data-server/libedataserver/e-source-mail-submission.h
/usr/include/evolution-data-server/libedataserver/e-source-mail-transport.h
/usr/include/evolution-data-server/libedataserver/e-source-mdn.h
/usr/include/evolution-data-server/libedataserver/e-source-memo-list.h
/usr/include/evolution-data-server/libedataserver/e-source-offline.h
/usr/include/evolution-data-server/libedataserver/e-source-openpgp.h
/usr/include/evolution-data-server/libedataserver/e-source-proxy.h
/usr/include/evolution-data-server/libedataserver/e-source-refresh.h
/usr/include/evolution-data-server/libedataserver/e-source-registry-watcher.h
/usr/include/evolution-data-server/libedataserver/e-source-registry.h
/usr/include/evolution-data-server/libedataserver/e-source-resource.h
/usr/include/evolution-data-server/libedataserver/e-source-revision-guards.h
/usr/include/evolution-data-server/libedataserver/e-source-security.h
/usr/include/evolution-data-server/libedataserver/e-source-selectable.h
/usr/include/evolution-data-server/libedataserver/e-source-smime.h
/usr/include/evolution-data-server/libedataserver/e-source-task-list.h
/usr/include/evolution-data-server/libedataserver/e-source-uoa.h
/usr/include/evolution-data-server/libedataserver/e-source-weather.h
/usr/include/evolution-data-server/libedataserver/e-source-webdav.h
/usr/include/evolution-data-server/libedataserver/e-source.h
/usr/include/evolution-data-server/libedataserver/e-time-utils.h
/usr/include/evolution-data-server/libedataserver/e-uid.h
/usr/include/evolution-data-server/libedataserver/e-url.h
/usr/include/evolution-data-server/libedataserver/e-webdav-discover.h
/usr/include/evolution-data-server/libedataserver/e-webdav-session.h
/usr/include/evolution-data-server/libedataserver/e-xml-document.h
/usr/include/evolution-data-server/libedataserver/e-xml-hash-utils.h
/usr/include/evolution-data-server/libedataserver/e-xml-utils.h
/usr/include/evolution-data-server/libedataserver/eds-version.h
/usr/include/evolution-data-server/libedataserver/libedataserver.h
/usr/include/evolution-data-server/libedataserverui/e-cell-renderer-color.h
/usr/include/evolution-data-server/libedataserverui/e-credentials-prompter-impl-google.h
/usr/include/evolution-data-server/libedataserverui/e-credentials-prompter-impl-password.h
/usr/include/evolution-data-server/libedataserverui/e-credentials-prompter-impl.h
/usr/include/evolution-data-server/libedataserverui/e-credentials-prompter.h
/usr/include/evolution-data-server/libedataserverui/e-trust-prompt.h
/usr/include/evolution-data-server/libedataserverui/e-webdav-discover-widget.h
/usr/include/evolution-data-server/libedataserverui/libedataserverui.h
/usr/lib64/libcamel-1.2.so
/usr/lib64/libebackend-1.2.so
/usr/lib64/libebook-1.2.so
/usr/lib64/libebook-contacts-1.2.so
/usr/lib64/libecal-1.2.so
/usr/lib64/libedata-book-1.2.so
/usr/lib64/libedata-cal-1.2.so
/usr/lib64/libedataserver-1.2.so
/usr/lib64/libedataserverui-1.2.so
/usr/lib64/pkgconfig/camel-1.2.pc
/usr/lib64/pkgconfig/evolution-data-server-1.2.pc
/usr/lib64/pkgconfig/libebackend-1.2.pc
/usr/lib64/pkgconfig/libebook-1.2.pc
/usr/lib64/pkgconfig/libebook-contacts-1.2.pc
/usr/lib64/pkgconfig/libecal-1.2.pc
/usr/lib64/pkgconfig/libedata-book-1.2.pc
/usr/lib64/pkgconfig/libedata-cal-1.2.pc
/usr/lib64/pkgconfig/libedataserver-1.2.pc
/usr/lib64/pkgconfig/libedataserverui-1.2.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/evolution-data-server/addressbook-backends/libebookbackendfile.so
/usr/lib64/evolution-data-server/addressbook-backends/libebookbackendgoogle.so
/usr/lib64/evolution-data-server/addressbook-backends/libebookbackendldap.so
/usr/lib64/evolution-data-server/addressbook-backends/libebookbackendwebdav.so
/usr/lib64/evolution-data-server/calendar-backends/libecalbackendcaldav.so
/usr/lib64/evolution-data-server/calendar-backends/libecalbackendcontacts.so
/usr/lib64/evolution-data-server/calendar-backends/libecalbackendfile.so
/usr/lib64/evolution-data-server/calendar-backends/libecalbackendgtasks.so
/usr/lib64/evolution-data-server/calendar-backends/libecalbackendhttp.so
/usr/lib64/evolution-data-server/camel-providers/libcamelimapx.so
/usr/lib64/evolution-data-server/camel-providers/libcamellocal.so
/usr/lib64/evolution-data-server/camel-providers/libcamelnntp.so
/usr/lib64/evolution-data-server/camel-providers/libcamelpop3.so
/usr/lib64/evolution-data-server/camel-providers/libcamelsendmail.so
/usr/lib64/evolution-data-server/camel-providers/libcamelsmtp.so
/usr/lib64/evolution-data-server/credential-modules/module-credentials-goa.so
/usr/lib64/evolution-data-server/libedbus-private.so
/usr/lib64/evolution-data-server/registry-modules/module-cache-reaper.so
/usr/lib64/evolution-data-server/registry-modules/module-gnome-online-accounts.so
/usr/lib64/evolution-data-server/registry-modules/module-google-backend.so
/usr/lib64/evolution-data-server/registry-modules/module-outlook-backend.so
/usr/lib64/evolution-data-server/registry-modules/module-secret-monitor.so
/usr/lib64/evolution-data-server/registry-modules/module-trust-prompt.so
/usr/lib64/evolution-data-server/registry-modules/module-webdav-backend.so
/usr/lib64/evolution-data-server/registry-modules/module-yahoo-backend.so
/usr/lib64/libcamel-1.2.so.60
/usr/lib64/libcamel-1.2.so.60.0.0
/usr/lib64/libebackend-1.2.so.10
/usr/lib64/libebackend-1.2.so.10.0.0
/usr/lib64/libebook-1.2.so.19
/usr/lib64/libebook-1.2.so.19.1.3
/usr/lib64/libebook-contacts-1.2.so.2
/usr/lib64/libebook-contacts-1.2.so.2.0.0
/usr/lib64/libecal-1.2.so.19
/usr/lib64/libecal-1.2.so.19.0.0
/usr/lib64/libedata-book-1.2.so.25
/usr/lib64/libedata-book-1.2.so.25.0.0
/usr/lib64/libedata-cal-1.2.so.28
/usr/lib64/libedata-cal-1.2.so.28.0.0
/usr/lib64/libedataserver-1.2.so.22
/usr/lib64/libedataserver-1.2.so.22.0.0
/usr/lib64/libedataserverui-1.2.so.1
/usr/lib64/libedataserverui-1.2.so.1.0.0

%files locales -f evolution-data-server.lang
%defattr(-,root,root,-)

