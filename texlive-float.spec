# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/float
# catalog-date 2009-09-26 09:33:53 +0200
# catalog-license lppl
# catalog-version 1.3d
Name:		texlive-float
Version:	1.3d
Release:	4
Summary:	Improved interface for floating objects
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/float
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/float.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/float.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/float.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.3d-2
+ Revision: 751926
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.3d-1
+ Revision: 718461
- texlive-float
- texlive-float
- texlive-float
- texlive-float

