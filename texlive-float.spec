%global tl_name float
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.3d
Release:	%{tl_revision}.1
Summary:	Improved interface for floating objects
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/float
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/float.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/float.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/float.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Improves the interface for defining floating objects such as figures and
tables. Introduces the boxed float, the ruled float and the plaintop
float. You can define your own floats and improve the behaviour of the
old ones. The package also provides the H float modifier option of the
obsolete here package. You can select this as automatic default with
\floatplacement{figure}{H}.

