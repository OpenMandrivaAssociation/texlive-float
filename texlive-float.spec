Name:		texlive-float
Version:	15878
Release:	2
Summary:	Improved interface for floating objects
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/float
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/float.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/float.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/float.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Improves the interface for defining floating objects such as
figures and tables. Introduces the boxed float, the ruled float
and the plaintop float. You can define your own floats and
improve the behaviour of the old ones. The package also
provides the H float modifier option of the obsolete here
package. You can select this as automatic default with
\floatplacement{figure}{H}.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/float/float.sty
%doc %{_texmfdistdir}/doc/latex/float/README
%doc %{_texmfdistdir}/doc/latex/float/float.pdf
#- source
%doc %{_texmfdistdir}/source/latex/float/float.dtx
%doc %{_texmfdistdir}/source/latex/float/float.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
