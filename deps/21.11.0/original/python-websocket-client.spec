Name:           python-websocket-client
Version:        1.4.2
Release:        1%{?dist}
Summary:        WebSocket client for Python with low level API options

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        ASL
URL:            https://github.com/websocket-client/websocket-client.git
Source:         %{pypi_source websocket-client}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'websocket-client' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-websocket-client
Summary:        %{summary}

%description -n python3-websocket-client %_description


%prep
%autosetup -p1 -n websocket-client-%{version}


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


%files -n python3-websocket-client -f %{pyproject_files}


%changelog
* Sun Jan 29 2023 Martin Juhl <m@rtinjuhl.dk> - 1.4.2-1
- Initial package