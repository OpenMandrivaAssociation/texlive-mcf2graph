%global tl_name mcf2graph
%global tl_revision 79502

Name:		texlive-%{tl_name}
Epoch:		1
Version:	5.33
Release:	%{tl_revision}.1
Summary:	Draw chemical structure diagrams with MetaPost
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/mcf2graph
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mcf2graph.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mcf2graph.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The Molecular Coding Format (MCF) is a linear notation for describing
chemical structure diagrams. This package converts MCF to graphic files
using MetaPost.

