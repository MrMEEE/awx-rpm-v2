Name:           python-twilio
Version:        7.15.3
Release:        1%{?dist}
Summary:        Twilio API client and TwiML generator

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/twilio/twilio-python/
Source:         %{pypi_source twilio}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'twilio' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-twilio
Summary:        %{summary}

%description -n python3-twilio %_description


%prep
%autosetup -p1 -n twilio-%{version}


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


%files -n python3-twilio -f %{pyproject_files}


%changelog
* Sun Jan 29 2023 Martin Juhl <m@rtinjuhl.dk> - 7.15.3-1
- Initial package