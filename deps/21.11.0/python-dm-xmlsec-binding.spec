Name:           python-dm-xmlsec-binding
Version:        2.2
Release:        1%{?dist}
Summary:        Cython/lxml based binding for the XML security library -- for lxml 3.x

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://pypi.org/project/dm.xmlsec.binding
Source:         %{pypi_source dm.xmlsec.binding}

BuildArch:      x86_64
BuildRequires:  python3-devel libxml2-devel xmlsec1-openssl-devel xmlsec1-devel gcc libtool-ltdl-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'dm-xmlsec-binding' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-dm-xmlsec-binding
Summary:        %{summary}

%description -n python3-dm-xmlsec-binding %_description


%prep
%autosetup -p1 -n dm.xmlsec.binding-%{version}
sed -i '/Md5/d' src/_xmlsec.c
sed -i '/Sha1/d' src/_xmlsec.c

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel

%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python3-dm-xmlsec-binding -f %{pyproject_files}


%changelog
* Fri Feb 24 2023 Martin Juhl <m@rtinjuhl.dk> - 2.2-1
- Initial package
