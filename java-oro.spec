Summary:	Full regular expressions API
Summary(pl.UTF-8):	Pełne API do wyrażeń regularnych
Name:		jakarta-oro
Version:	2.0.8
Release:	2
License:	Apache License
Group:		Development/Languages/Java
Source0:	http://www.apache.org/dist/jakarta/oro/%{name}-%{version}.zip
# Source0-md5:	af58ac4811ee023b6211446eb7b7fff2
URL:		http://jakarta.apache.org/oro/
BuildRequires:	ant >= 1.5
BuildRequires:	jdk
BuildRequires:	jpackage-utils
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	jre
BuildArch:	noarch
ExclusiveArch:	i586 i686 pentium3 pentium4 athlon %{x8664} noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Jakarta-ORO Java classes are a set of text-processing Java classes
that provide Perl5 compatible regular expressions, AWK-like regular
expressions, glob expressions, and utility classes for performing
substitutions, splits, filtering filenames, etc. This library is the
successor to the OROMatcher, AwkTools, PerlTools, and TextTools
libraries from ORO, Inc. (http://www.oroinc.com/). They have been
donated to the Jakarta Project by Daniel Savarese
(http://www.savarese.org/), the copyright holder of the ORO libraries.
Daniel will continue to participate in their development under the
Jakarta Project.

%description -l pl.UTF-8
Klasy Javy Jakarta-ORO to zestaw klas do przetwarzania tekstu
udostępniający wyrażenia regularne zgodne z Perlem 5, awkowe wyrażenia
regularne, wyrażenia glob oraz klasy narzędziowe do wykonywania
podstawień, podziałów, filtrowania nazw plików itp. Ta biblioteka jest
następcą bibliotek OROMatcher, AwkTools, PerlTools i TextTools firmy
ORO Inc. (http://www.oroinc.com/). Zostały podarowane projektowi
Jakarta przez DAniela Savarese (http://www.savarese.org/), właściciela
praw autorskich do bibliotek ORO. Daniel będzie nadal udzielał się
przy rozwoju tych bibliotek w projekcie Jakarta.

%package javadoc
Summary:	Jakarta-ORO API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki Jakarta-ORO
Group:		Documentation
Requires:	jpackage-utils

%description javadoc
Jakarta-ORO API documentation.

%description javadoc -l pl.UTF-8
Dokumentacja API biblioteki Jakarta-ORO.

%prep
%setup -q
find . -name "*.jar" -exec rm -f {} \;
for dir in `find . -type d -name CVS`; do rm -rf $dir; done
for file in `find . -type f -name .cvsignore`; do rm -rf $file; done

%build
unset CLASSPATH || :
export JAVA_HOME="%{java_home}"
%ant -Dfinal.name=oro jar javadocs

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_javadir},%{_javadocdir}/%{name}-%{version}}

cp oro.jar $RPM_BUILD_ROOT%{_javadir}/oro-%{version}.jar
ln -sf oro-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/oro.jar

cp -R docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COMPILE ISSUES README TODO CHANGES CONTRIBUTORS LICENSE STYLE
%{_javadir}/*.jar

%files javadoc
%defattr(644,root,root,755)
%doc %{_javadocdir}/%{name}-%{version}
