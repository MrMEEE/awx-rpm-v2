Name:           python-channels
Version:        3.0.5
Release:        1%{?dist}
Summary:        Brings async, event-driven capabilities to Django 3.2 and up.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD
URL:            http://github.com/django/channels
Source:         %{pypi_source channels}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'channels' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-channels
Summary:        %{summary}

%description -n python3-channels %_description


%prep
%autosetup -p1 -n channels-%{version}


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


%files -n python3-channels -f %{pyproject_files}


%changelog
* Sun Jan 29 2023 Martin Juhl <m@rtinjuhl.dk> - 3.0.5-1
- Initial package