Summary:	Dictionaries for SKK (Simple Kana-Kanji conversion program)
Summary(pl.UTF-8):	Słowniki dla SKK (konwersji Simple Kana-Kanji)
Name:		skkdic
Version:	20110722
Release:	1
License:	GPL v2+
Group:		Libraries
# To create source tarball, use Source10
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	085e0bceeffa1a24ead6595f6d4629d1
Source10:	create-%{name}-source.sh
Source20:	README-%{name}.rh.ja
URL:		http://openlab.ring.gr.jp/skk/skk/dic/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package includes the SKK dictionaries, including the large
dictionary SKK-JISYO.L and pubdic+ dictionary.

%description -l pl.UTF-8
Ten pakiet zawiera słowniki SKK, w tym duży słownik SKK-JISYO.L
oraz pubdic+.

%prep
%setup -q
cp -p %{SOURCE20} .
mv zipcode/README.ja README-zipcode.ja

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/skk

for f in SKK-JISYO* zipcode/SKK-JISYO* ; do
	install -p -m 644 $f $RPM_BUILD_ROOT%{_datadir}/skk
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog* edict_doc.txt
%lang(ja) %doc README-skkdic.rh.ja README-zipcode.ja
%{_datadir}/skk
